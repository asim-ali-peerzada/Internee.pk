from django import forms
from .models import CustomUserprofile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUserprofile
        fields = ['name', 'bio', 'skills', 'description', 'profile_photo']