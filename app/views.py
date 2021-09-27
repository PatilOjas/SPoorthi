from django.shortcuts import redirect, render
from django.shortcuts import render
from .forms import RegistrationForm
from django.core.mail import send_mail
from django.conf import settings
from cricScore import LiveScoreCricket



def registrationPage(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			subject = "Successfully registered for SPoorthi!"
			message = f"Greetings From Spoorthi SPIT,\nHello {request.POST['fullName']}, you have succesfully registered for {request.POST['event']}.\nPlease Show this email at the time of Event.\nSee you at SPoorthi from 13-31st January'20.\nSports Team At SPIT"
			# from_email = settings.EMAIL_HOST_USER
			# mail = send_mail(subject, message, from_email, [request.POST['email']], fail_silently=False)
		
	return render(request, 'index.html')

# def homePage(request):
# 	return render(request, '')

def scorepage(request):
	L = LiveScoreCricket()
	data = L.fetchScore()
	return render(request, 'livescore.html', {'data': data, 'keys': data.keys()})