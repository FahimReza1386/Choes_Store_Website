from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User= get_user_model()

class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User  
        fields=["email",]


    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class UserLoginForm(forms.ModelForm):
    password= forms.PasswordInput()
    class Meta:
        model=User
        fields=["email", "password"]

