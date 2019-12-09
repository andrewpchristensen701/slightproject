from django import forms


class MakeTweet(forms.Form):
    message = forms.CharField(widget=forms.Textarea, max_length=280)