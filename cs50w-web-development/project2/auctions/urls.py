from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name="auctions"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new, name="new"),
    path("auction/<int:auction_id>", views.auction, name="auction"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("addtowatchlist/<int:auction_id>", views.addtowatchlist, name="addtowatchlist"),
    path("removefromwatchlist/<int:auction_id>", views.removefromwatchlist, name="removefromwatchlist"),
    path("categories", views.categories, name="categories"),
    path("categories/<int:category_id>", views.category_auctions, name="category_auctions"),
    path("close/<int:auction_id>", views.close_auction, name="close_auction"),
    path("add_comment/<int:auction_id>", views.add_comment, name="add_comment"),
    path("mybids", views.my_bids, name="my_bids")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)