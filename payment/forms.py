from django import forms
from django.forms import HiddenInput
from payment.models import Comment


class ContactForm(forms.Form):
    email = forms.EmailField()
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea(attrs={"rows": 2}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = [
            "id",
        ]
        widgets = {
            "product":forms.HiddenInput()
        }


class CardForm(forms.Form):
    user_card = forms.CharField(max_length=16)
    prepaid_card = forms.CharField(max_length=8)
