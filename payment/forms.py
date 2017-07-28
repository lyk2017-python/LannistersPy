from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField()
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea(attrs={"rows": 2}))


