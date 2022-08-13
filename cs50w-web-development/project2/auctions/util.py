import re
from .models import User, Auction, Bid, Comment, Category, Watchlist


def in_watchlist(user_id, auction_id):
    """
    Util function to check if a specific item is in a user watchlist
    :param user_id: The user identifier
    :type user_id: int
    :param auction_id: The auction identifier
    :type auction_id: int
    :return: True if the item in the user watchlist false otherwise
    :rtype: boolean
    """
    in_watchlist = Watchlist.objects.filter(user=user_id, item=auction_id)
    if len(in_watchlist) > 0:
        return True
    else:
        return False