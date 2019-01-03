from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(max_length=60,
            widget=forms.TextInput(attrs={'name':'name'}))
    
    password = forms.CharField(max_length=100,
            widget=forms.TextInput(attrs={'name':'password'}))
    
class SigninForm(forms.Form):
    name = forms.CharField(max_length=60,
            widget=forms.TextInput(attrs={'name':'name'}))
    
    password = forms.CharField(max_length=100,
            widget=forms.TextInput(attrs={'name':'password'}))
    
    cpassword = forms.CharField(max_length=100,
            widget=forms.TextInput(attrs={'name':'cpassword'}))