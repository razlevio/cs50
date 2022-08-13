from django import forms


class NewPage(forms.Form):
    title = forms.CharField(label="Title", max_length=255)
    md = forms.CharField(label="Page markdown", widget=forms.Textarea(
        attrs={'placeholder': 'Insert page content in markdown format'}))
