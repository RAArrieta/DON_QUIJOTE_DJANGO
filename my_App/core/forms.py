from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})




# from django import forms
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import User

# class CustomAuthenticationForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ["username", "password"]
#         widgets = {
#             "username": forms.TextInput(attrs={"class": "form-control"}),
#             "password": forms.PasswordInput(attrs={"class": "form-control"}),
#         }


