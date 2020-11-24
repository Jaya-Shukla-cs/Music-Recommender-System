from django.contrib.auth.models import Permission, User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Music(models.Model):
	title   	= models.CharField(max_length=200)
	album  		= models.CharField(max_length=100)
	music_logo  = models.FileField() 
	artist = models.CharField(max_length=10000)

	def __str__(self):
		return self.title

class Myrating(models.Model):
	user   	= models.ForeignKey(User,on_delete=models.CASCADE) 
	music 	= models.ForeignKey(Music,on_delete=models.CASCADE)
	rating 	= models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(0)])
		
