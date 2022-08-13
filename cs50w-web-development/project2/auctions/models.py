from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    A class to represent a user
    The class inheriths from django super class AbstractUser.
    """
    def __str__(self):
        return f"{self.username}"

class Auction(models.Model):
    """
    Represent every auction on the web application
    The model inherits from django models class
    """
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller")
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1000)
    initial_price = models.IntegerField()
    last_bid_price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="auctions/static/auctions/images/", null=True, blank=True) # CONSIDER REMOVE BLANK AND NULL MAY NOT BE NEEDED
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="cat")
    created_date = models.DateTimeField(auto_now_add=True)
    num_of_bids = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    winner_user_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"AuctionID: {self.id}, Item: {self.title}, InitialPrice: {self.initial_price}, Category: {self.category}"

class Bid(models.Model):
    """
    Represents bids information for each auction
    """
    auction_id = models.ForeignKey("Auction", on_delete=models.CASCADE, related_name="auction_id")
    price = models.IntegerField()
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id")
    bid_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"BidPrice: {self.price}, Bidder: {self.buyer}, BidDate: {self.bid_date}"

class Comment(models.Model):
    """ Represents comments on auctions """
    auction = models.ForeignKey("Auction", on_delete=models.CASCADE, related_name="auctionID")
    commenter = models.ForeignKey("User", on_delete=models.CASCADE, related_name="commenter")
    comment = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.comment}"


class Category(models.Model):
    """ Represents categories for auctions """
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Watchlist(models.Model):
    """ Represnts users watchlists """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    item = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="item")

    def __str__(self):
        return f"UserID: {self.user.id}, Item: {self.item.title}"