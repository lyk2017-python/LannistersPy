from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.db.models import F

from payment.models import *


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
            "product": forms.HiddenInput()
        }


class CardForm(forms.Form):
    prepaid_card = forms.CharField(max_length=8, min_length=8)
    user_card = forms.CharField(max_length=16, min_length=16)

    def clean_user_card(self):
        x = self.data.get("user_card")
        uc = UserCard.objects.filter(card_number=x)
        if uc.exists():
            return uc.first()
        else:
            raise forms.ValidationError("User Card Not Found.")

    def clean_prepaid_card(self):
        x = self.data.get("prepaid_card")
        pc = PrepaidCard.objects.filter(barcode=x)
        if pc.exists() and not pc.first().is_used:
            return pc.first()
        else:
            raise forms.ValidationError("Prepaid Card Not Found or Already Used.")

    def save(self):
        user_card = self.cleaned_data["user_card"]
        prepaid_card = self.cleaned_data["prepaid_card"]

        with transaction.atomic():
            user_card.balance = F("balance") + prepaid_card.value
            user_card.save(update_fields=["balance"])
            prepaid_card.is_used = True
            prepaid_card.save(update_fields=["is_used"])
            t = Transaction.objects.create(user_card=user_card, prepaid_card=prepaid_card)
        return t

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()