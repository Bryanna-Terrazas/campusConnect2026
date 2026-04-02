from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .models import Posts

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['bio', 'age', 'phone']

class PostingToFeed(forms.ModelForm):
	class Meta:
		model = Posts
		fields = ['subject', 'bodyofpost']