from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'form-name', 'name':'form-name', 'placeholder':'Name..'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'id':'form-email', 'name':'form-email', 'placeholder':'Email..' }))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'form-phone', 'name':'form-phone', 'placeholder':'Subject..'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':'6', 'id':'form-message', 'name':'form-message', 'placeholder':'Your Message Here...'})) 
