from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User
from .models import administrator, participant

# class participantForm(forms.ModelForm):
#     class Meta:
#         model = participant
#         fields = ['full_name','score']

class UserRegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class loginForm(forms.Form):
    username = forms.CharField(max_length = 200)
    password = forms.CharField(widget = forms.PasswordInput)

    def clean_username(self):
        inst_username = self.cleaned_data.get("username")
        return inst_username

    def clean_password(self):
        inst_password = self.cleaned_data.get("password")
        return inst_password

class participantForm(forms.ModelForm):
    class Meta:
        model = participant
        fields = ['full_name','score']#attributes

    def clean_full_name(self):
        #.cleaned_data() returns a dictionary with the attributes of the participantForm cleaned and the function is mostly defined in the super class of participantForm ie, forms.Model form
        inst_full_name = self.cleaned_data.get('full_name')
        return inst_full_name

    def clean_score(self):
        inst_score = self.cleaned_data.get('score')
        if inst_score <= 50.00 and inst_score >= 0.00:
            return inst_score
        else:
            raise ValidationError("Please enter a meaningful score between 0 and 50")
