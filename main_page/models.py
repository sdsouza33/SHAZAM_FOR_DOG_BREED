from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
from main_page.breed_detect import detect


#from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	img1 = models.ImageField(upload_to='dog_image', default='default.jpg')
	breed = models.CharField(max_length=100, default=None, blank=True, null=True)
	name = models.CharField(max_length=100)
	contact = models.IntegerField()
	address = models.TextField()
	additional_info = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now())
	


	def __str__(self):
		return self.breed
		