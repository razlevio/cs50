from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Auction, Bid, Comment, Category, Watchlist
from .forms import NewAuction
from . import util


def login_view(request):
    """
    The login function responsible for logging in users
    """

    # POST request
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })

    # GET request
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    """
    Logging out user from the web application
    """
    logout(request)
    return HttpResponseRedirect(reverse("auctions:index"))


def register(request):
    """
    Register new user to the web application
    """

    # POST request
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def index(request):
    """
    Shows grid of active auctions
    """
    return render(request, "auctions/index.html", {
        "items": Auction.objects.all()
    })


def auction(request, auction_id):
    """
    Auction infromation page
    Users can see all of the detailes about the auction and make their own bid if they want to
    """

    # Extracting data about the auction from the database
    user_id = request.user.id
    listing = Auction.objects.filter(id=auction_id)
    bids = Bid.objects.filter(auction_id=auction_id)
    comments = Comment.objects.filter(auction=auction_id)
    in_watchlist = util.in_watchlist(user_id, listing[0].id)

    # POST request
    if request.method == "POST":
        # Updating latest bid price and num of bids from the bids model
        if len(bids) > 0:
            listing.update(last_bid_price=bids[len(bids)-1].price, num_of_bids=len(bids))

        # Extracting the user new bid if he decided to bid on the item
        bid = request.POST.get("bid_price")

        # Data validation of the input
        try:
            bid = int(bid)
        except ValueError:
            return render(request, "auctions/auction.html", {
                "listing": listing[0],
                "error": "Wrong input number for a bid",
                "user_obj": request.user,
                "comments": comments
            })

        # If the new bid is greater than the last bid and the initial price, add the bid
        if bid > listing[0].initial_price and bid > listing[0].last_bid_price:
            new_bid = Bid()
            new_bid.auction_id = listing[0]
            new_bid.price = bid
            new_bid.buyer = request.user
            new_bid.save()
            bids = Bid.objects.filter(auction_id=auction_id)
            listing.update(last_bid_price=bid, num_of_bids=len(bids))
            # Render the auction page with success message
            return render(request, "auctions/auction.html", {
                "listing": listing[0],
                "message": "You placed your bid successfully",
                "user_obj": request.user,
                "comments": comments
            })

        # User tried to bid a price that is lower than the last bid, render the auction page with error message
        else:
            return render(request, "auctions/auction.html", {
                "listing": listing[0],
                "error": "Bid price should be greater than initial price and the last bid price",
                "user_obj": request.user,
                "comments": comments
            })

    # GET request
    # Render the auction page with the relevant data
    else:
        if len(bids) > 0:
            # Checking if the user that visit this auction won the item, and if he does render a winner message
            if listing[0].status == False and request.user.id == listing[0].winner_user_id:
                return render(request, "auctions/auction.html", {
                    "listing": listing[0],
                    "in_watchlist": in_watchlist,
                    "user_obj": request.user,
                    "comments": comments,
                    "winner": f"You won this auction for ${listing[0].last_bid_price}"
                })

            # Render the page with relevant data
            listing.update(last_bid_price=bids[len(bids)-1].price, num_of_bids=len(bids))
            return render(request, "auctions/auction.html", {
                "listing": listing[0],
                "in_watchlist": in_watchlist,
                "user_obj": request.user,
                "comments": comments,
            })

        # Render the page with relevant data
        else:
            return render(request, "auctions/auction.html", {
                "listing": listing[0],
                "in_watchlist": in_watchlist,
                "user_obj": request.user,
                "comments": comments,
            })


@login_required(login_url='/login')
def new(request):
    """
    Create new auction listing
    Users specify a title for the listing, a text-based description, and what the starting bid price should be.
    Also users load an image for the listing and select the category of the item
    """

    # POST request
    if request.method == "POST":
        # Creating new auction model object
        it = Auction()

        # Creating new form for the item
        item = NewAuction(request.POST, request.FILES)

        # Check if the form fields inputs are valid
        if item.is_valid():
            # Saving the input inserted into the form to the new auction model object
            it.seller = request.user
            it.title = item.cleaned_data["title"]
            it.description = item.cleaned_data["description"]
            it.initial_price = item.cleaned_data["initial_price"]
            it.image = item.cleaned_data["image"]
            it.category = item.cleaned_data["category"]
            it.save()

        # Rendering the index page with the new auction included and an success message
        return render(request, "auctions/index.html", {
            "message": "Item added successfuly",
            "items": Auction.objects.all()
        })

    # GET request
    # Render the form so the user could add its item
    return render(request, "auctions/new.html", {
        "form": NewAuction
    })


@login_required(login_url='/login')
def watchlist(request):
    """
    Users who are signed in should be able to visit a Watchlist page,
    which should display all of the listings that a user has added to their watchlist.
    Clicking on any of those listings should take the user to the listing page.
    """

    # Extracting data about the auction and the user that initate the request
    user_id = request.user.id
    auctions = Watchlist.objects.filter(user=user_id)

    # Rendering the watch list
    return render(request, "auctions/watchlist.html", {
        "auctions": auctions,
        "num_of_auctions": len(auctions)
    })


@login_required(login_url="/login")
def addtowatchlist(request, auction_id):
    """
    Adding item to the user watchlist
    """

    # Extracting data about the auction and the user that initate the request
    user_id = request.user.id
    auction = Auction.objects.get(id=auction_id)

    # If the user tries to add his own item to the watchlist through URL manipulation
    # Render the item page and don't add the item to the user watchlist
    if auction.seller == request.user:
        return HttpResponseRedirect(reverse("auctions:auction", args=[auction_id]))

    # Checking if the item is already in the watchlist of the user
    # I am doing so to prevent users add duplications thorugh URL manipulation
    already = util.in_watchlist(user_id, auction_id)
    # If the item is not in the user watchlist add it to the watchlist and render thw watchlist
    if not already:
        new_item = Watchlist()
        new_item.user = request.user
        new_item.item = Auction.objects.get(id=auction_id)
        new_item.save()
        return HttpResponseRedirect(reverse("auctions:watchlist"))
    # If the item is already in the user watchlist render the auction page and don't add the item again to the user watchlist
    else:
        return HttpResponseRedirect(reverse("auctions:auction", args=[auction_id]))


@login_required(login_url="/login")
def removefromwatchlist(request, auction_id):
    """
    Remove item from user watchlist
    """
    Watchlist.objects.filter(user=request.user.id, item=auction_id).delete()
    return HttpResponseRedirect(reverse("auctions:watchlist"))


def categories(request):
    """
    Render a page that shows a list of all categories in the web app
    """
    return render(request, "auctions/categories.html", {
        "categories": Category.objects.all()
    })


def category_auctions(request, category_id):
    """
    If the user clicked on specific category, render a page with all of the auctions in that category
    """
    return render(request, "auctions/index.html", {
        "items": Auction.objects.filter(category=category_id)
    })


@login_required(login_url="/login")
def close_auction(request, auction_id):
    """
    Close an active auction by the user created it
    Let the user know the amount of the highest bidder and who is the user that won the item
    """

    if request.method == "POST":
        bids = Bid.objects.filter(auction_id=auction_id)
        auct = Auction.objects.filter(id=auction_id)

        # There is atleast one bid on this auction
        if len(bids) > 0:
            auct.update(status=False, winner_user_id=bids[len(bids)-1].buyer.id)
        else:
            auct.update(status=False, winner_user_id=0)

        return render(request, "auctions/auction_summary.html", {
            "message": "Your Auction closed successfully",
            "auction": auct[0],
            "winner_bid":  bids[len(bids)-1]
        })

    # GET request simply render the auction page without doing anything
    else:
        return HttpResponseRedirect(reverse("auctions:auction", args=[auction_id]))

@login_required(login_url="/login")
def add_comment(request, auction_id):
    """
    Adding a comment to an auction page
    """

    # Extracting relevant data about the auction and the comments
    listing = Auction.objects.get(id=auction_id)
    comments = Comment.objects.filter(auction=auction_id)
    user_comment = request.POST.get("comment")

    # POST request
    if request.method == "POST":
        # Comment input validation
        if len(user_comment) < 5:
            return render(request, "auctions/auction.html", {
                "listing": listing,
                "user_obj": request.user,
                "comments": comments,
                "error": "Comment not long enough"
        })

        # Passed the input validation, add the comment to the database and render the auction page to include the new comment
        new_comment = Comment(comment=user_comment, auction=Auction.objects.get(id=auction_id), commenter=request.user)
        new_comment.save()
        return render(request, "auctions/auction.html", {
            "listing": listing,
            "user_obj": request.user,
            "comments": comments,
            "message": "Comment added successfully"
        })

    # GET request
    else:
        return HttpResponseRedirect(reverse("auctions:auction", args=[auction_id]))


@login_required(login_url="/login")
def my_bids(request):
    """
    Rendering a page so users can track all of their bids
    """
    bids = Bid.objects.filter(buyer=request.user)
    return render(request, "auctions/mybids.html", {
        "bids": bids,
        "user_id": request.user.id
    })