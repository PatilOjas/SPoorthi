from django import forms
from .models import RegistrationModel


class RegistrationForm(forms.ModelForm):
	class Meta:
		model = RegistrationModel
		fields = ('event', 'fullName', 'email', 'mobNo', 'collegeName', 'secondPlayerName', 'secondPlayerMobNo')
