from django import forms

class ProfileForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'form-full_name', 'name':'form-full_name', 'placeholder':'Name'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'form-country', 'name':'form-country', 'placeholder':'Country'}))
    company = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'form-company', 'name':'form-company', 'placeholder':'Company'}))
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'form-phone_no', 'name':'form-phone_no', 'placeholder':'Phone Number'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'form-address', 'name':'form-address', 'placeholder':'Address'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'id':'form-email', 'name':'form-email', 'placeholder':'Email'}))
    
