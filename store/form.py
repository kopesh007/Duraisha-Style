from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(label="NAME", max_length=100,required=True)
    email=forms.EmailField(label="EMAIL",required=True)
    subject=forms.CharField(label="SUBJECT",required=True)
    mess=forms.CharField(label="MESSAGE", required=False)