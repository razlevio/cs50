from django.shortcuts import render
from random import choice
from . import util
import markdown2


def index(request):
    """
    Display a list of all encyclopedia entries
    :param request: The HTTP request
    :type request: HTTP request
    :return: All encyclopedia entries names
    :rtype: list
    """

    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })


def get_entry(request, title):
    """
    Get information about specific entry in the wiki, if there is no
    such entry render an error message
    :param request: The HTTP request
    :type request: HTTP request
    :param title: The entry title
    :type title: str
    :return: Render the entry page with correct data or render error message
    """
    entry = util.get_entry(title)
    if entry:
        # Convert the markdown into HTML
        entry = markdown2.markdown(entry)
        # Render the entry html page with the provided title and the HTML details of the entry
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": entry
        })
    # Entry no found and generating an error
    else:
        return render(request, "encyclopedia/error.html", {
            "message": "404 Page Not Found"
        })


def search(request):
    """
    Search the wiki for specific entry by provided title
    :param request: The HTTP request
    :type request: HTTP request
    :return: Render the entry page with correct data or render error message
    """
    # Getting the list of available entires in order to validate search
    entries = util.list_entries()
    entries = [entry.lower() for entry in entries]
    # Getting the search query inserted by the user
    query = request.GET.get("q").lower()

    # If we have the query provided as entry render the entry page
    if query in entries:
        return get_entry(request, query)
    # Render the closets possible entries
    else:
        substrings = []
        # Traversing entries to check if some entries related to the query
        for entry in entries:
            if query in entry:
               # If the entry is related to the query add it to the list
                substrings.append(entry)
        # Render the search page with the related entires only
        return render(request, "encyclopedia/search.html", {
            "entries": substrings
        })


def new(request):
    """
    Create a new markdown file by gathering the title and the markdown content of the entry from the user
    :param request: The HTTP request
    :type request: HTTP request
    :returns: If GET request render the new page form, if POST create new entry
    """
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")

    # Route accessed by POST request
    else:
        # Extract the information from the form
        form = request.POST
        title = form["title"].lower()
        content = form["md"]

        # Check if this encyclopedia entry already exists
        entries = util.list_entries()

        # forced lowercase for preventing casing issues
        entries = [entry.lower() for entry in entries]

        # Checking if the new page already exists and if it does returns error message
        if title in entries:
            return render(request, "encyclopedia/error.html", {
                "message": "Error, page already exists"
            })
        # Entry not exists so saving the entry md file to the disk and render the new entry
        else:
            util.save_entry(title, content)
            return get_entry(request, title)


def edit(request, title):
    """
    Edit existing page content
    :param request: The HTTP request
    :type request: HTTP request
    :param title: The page title that we are about to edit
    :type title: str
    :returns: If GET request render edit page, if POST update the content of the page
    """

    if request.method == "GET":
        # Get current page markdown content
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })

    # Route accessed by POST request so update the new markdown content
    else:
        form = request.POST
        content = form["content"]
        util.save_entry(title, content)
        return get_entry(request, title)


def random(request):
    """ Display random encyclopedia entry """

    entries = util.list_entries()
    rnd = choice(entries)
    return get_entry(request, rnd)