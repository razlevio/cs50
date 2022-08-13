from django import forms
from django.forms import ModelForm
from .models import User, Auction, Bid, Comment, Category, Watchlist


class NewAuction(forms.ModelForm):
    """
    Django form to populate the new auction item
    """
    class Meta:
        model = Auction
        fields = ["title", "description", "initial_price", "image", "category"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "name": "title"}),
            "description": forms.Textarea(attrs={"class": "form-control", "name": "description"}),
            "initial_price": forms.NumberInput(attrs={"class": "form-control", "name": "initial_price"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control-file", "name": "image"}),
            "category": forms.Select(attrs={"class": "form-control", "name": "category"}),
        }
