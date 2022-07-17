from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=64, label='username')
    password = forms.CharField(max_length=64, widget=forms.PasswordInput, label='password')
