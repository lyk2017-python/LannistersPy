from django import forms
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
    prepaid_card = forms.CharField(max_length=16, min_length=16)
    user_card = forms.CharField(max_length=8, min_length=8)

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
        if pc.exists():
            return pc.first()
        else:
            raise forms.ValidationError("Prepaid Card Not Found.")

    def save(self):
        cd = self.cleaned_data["user_card"]
        pcd = self.cleaned_data["prepaid_card"]

        with transaction.atomic():
            cd.balance = F("balance") + pcd.balance
            cd.save(update_fields=["balance"])
            pcd.delete()
        return cd
