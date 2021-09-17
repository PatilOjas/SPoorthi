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
