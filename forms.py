from django import forms
from django.contrib.auth.models import User
from .models import News
class RegistrationForm(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput())

        class Meta:
            model = User
            fields = ['username', 'first_name', 'last_name', 'email', 'password']
            
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']
