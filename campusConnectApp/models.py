from django.db import models
from django.contrib.auth.models import User 

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	bio = models.TextField(blank = True)
	age = models.IntegerField(null = True, blank = True)
	phone = models.TextField(blank = True)

	def __str__(self):
		return self.user.username

class User(models.Model):
	first_name = models.TextField(blank = True)
	last_name = models.TextField(blank = True)
	email = models.TextField(blank = True)

class Posts(models.Model):
	subject = models.TextField(blank = True)
	bodyofpost = models.TextField(blank = True, null = True)
