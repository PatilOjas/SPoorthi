from django.shortcuts import redirect, render
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import RegistrationForm

import os

from sheet import SheetEditor


def registrationPage(request, name='*'):
	s1 = SheetEditor(sheetName="Site Feature Testing", sheet="Sheet1")
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			q = form.save()
			s1.wks.update(f"A{len(s1.wks.get_all_records()) + 2}:G{len(s1.wks.get_all_records()) + 2}", 
			[[q.playerId, q.fullName, q.email, q.collegeName, q.mobNo, q.event, str(q.datetimestamp)]])
			
			subject = "Successfully registered for SPoorthi!"
			message = f"Greetings From Spoorthi SPIT,\nHello {request.POST['fullName']}, you have succesfully registered for {request.POST['event']}.\nPlease Show this email at the time of Event.\nSee you at SPoorthi from 13-31st January'20.\nSports Team At SPIT"
			# from_email = settings.EMAIL_HOST_USER
			# mail = send_mail(subject, message, from_email, [request.POST['email']], fail_silently=False)
			return redirect('events')
	
	if name == '*':
		return render(request, 'index.html')
	else:
		return render(request, 'index.html')

def homePage(request):
	return render(request, 'home.html')

# def liveNews(request):
# 	return render(request, 'livescore.html', {'data': data})

def gallery(request):
	data = {
		'glimpse': os.listdir(path='./static/images/glimpse'),
		'agility2021': os.listdir(path='./static/images/agility2021'),
	}
	
	return render(request, 'gallery.html', data)

def eventPage(request, name=""):
	if name=="":
		return render(request, 'events.html')
	else:
		context = {}
		#get the event details by event name and add to context
		return render(request, 'event_details.html', context)