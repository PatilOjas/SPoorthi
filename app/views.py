from django.shortcuts import redirect, render
from django.shortcuts import render
from .forms import RegistrationForm
from .models import EventModel
from django.core.mail import send_mail
from django.conf import settings

from .forms import RegistrationForm

import os

from sheet import SheetEditor


def registrationPage(request, name='*'):
	offset = 2
	sheet_name = "SPoorthi"
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			saved_data = form.save()
			
			if saved_data.event == "Turf Cricket":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.fullName, saved_data.email, saved_data.collegeName, saved_data.mobNo, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Turf Football":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.fullName, saved_data.email, saved_data.collegeName, saved_data.mobNo, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Volleyball":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.fullName, saved_data.email, saved_data.collegeName, saved_data.mobNo, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Badminton (Singles)":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.fullName, saved_data.email, saved_data.collegeName, saved_data.mobNo, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Badminton (Doubles)":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.fullName, saved_data.email, saved_data.collegeName, saved_data.mobNo, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Carrom (Singles)":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.fullName, saved_data.email, saved_data.collegeName, saved_data.mobNo, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Carrom (Doubles)":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.fullName, saved_data.email, saved_data.collegeName, saved_data.mobNo, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Athletics":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.fullName, saved_data.email, saved_data.collegeName, saved_data.mobNo, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Chess":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.fullName, saved_data.email, saved_data.collegeName, saved_data.mobNo, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Dodgeball":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.fullName, saved_data.email, saved_data.collegeName, saved_data.mobNo, saved_data.event, str(saved_data.datetimestamp)]])
			

			subject = "Successfully registered for SPoorthi!"
			message = f"Greetings From Spoorthi SPIT,\nHello {saved_data.fullName}, you have succesfully registered for {saved_data.event}.\nPlease Show this email at the time of Event.\nSee you at SPoorthi from 13-31st January'20.\nSports Team At SPIT"
			# from_email = settings.EMAIL_HOST_USER
			# mail = send_mail(subject, message, from_email, [request.POST['email']], fail_silently=False)
			return redirect('events')
	
	# if name == '*':
	return render(request, 'index.html')
	# else:
	# 	return render(request, 'index.html')




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
		context = {}
		allEvents = EventModel.objects.all()
		context['allEvents'] = allEvents
		return render(request, 'events.html', context)
	else:
		context = {}

		#get the event details by event name and add to context
		getEvent = EventModel.objects.get(eventName=name)
		context['item'] = getEvent
		return render(request, 'event_details.html', context)