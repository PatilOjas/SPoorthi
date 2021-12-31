from django.db import models
class RegistrationModel(models.Model):
	fullName = models.CharField(max_length=100, null=False, blank=False)
	email = models.EmailField(null=False, blank=False)
	collegeName = models.CharField(max_length=100, null=False, blank=False)
	mobNo = models.CharField(max_length=15, null=False, blank=False)
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
	eventCoOrdinator2 = models.CharField(max_length=50)
	eventCoOrdinator2Mob = models.CharField(max_length=15)
	poster = models.ImageField(upload_to="media")

	def __str__(self):
		return self.eventName