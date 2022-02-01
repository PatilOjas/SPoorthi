from distutils.command import upload
from django.db import models
from app.models import *


class RegistrationModel(models.Model):
	playerId = models.AutoField(primary_key=True)
	email = models.EmailField(null=False, blank=False)
	fullName = models.CharField(max_length=100, null=False, blank=False)
	mobNo = models.CharField(max_length=15, null=False, blank=False)
	secondPlayerName = models.CharField(max_length=100, blank=True)
	secondPlayerMobNo = models.CharField(max_length=15, blank=True)
	collegeName = models.CharField(max_length=100, null=False, blank=False)
	event = models.CharField(max_length=50, null=False, blank=False)
	datetimestamp = models.DateTimeField(auto_now=True)

	
	def __str__(self):
		return self.fullName

class EventModel(models.Model):
	eventId = models.AutoField(primary_key=True)
	eventName = models.CharField(max_length=100)
	eventDesc = models.CharField(max_length=1000)
	eventCoOrdinator1 = models.CharField(max_length=50)
	eventCoOrdinator1Mob = models.CharField(max_length=15)
	eventCoOrdinator2 = models.CharField(max_length=50, blank=True)
	eventCoOrdinator2Mob = models.CharField(max_length=15, blank=True)
	poster = models.ImageField(upload_to="media")

	def __str__(self):
		return self.eventName

class ImageModel(models.Model):
	imageId = models.AutoField(primary_key=True)
	image = models.ImageField(upload_to="images")
	Classes = [
		('SPoorthi', 'SPoorthi 2022'),
		('Agility', 'Agility 2021'),
		('Glimpse', 'Glimpse of Past Years')
	]
	imageClass = models.CharField(max_length=10, choices=Classes)
	
	def __str__(self):
		return self.imageClass +" " + str(self.imageId)
	