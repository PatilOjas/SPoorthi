from django.shortcuts import redirect, render
from django.shortcuts import render
from .forms import RegistrationForm
from .models import EventModel, ImageModel
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib import messages

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
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Turf Football":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Volleyball":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Badminton (S)":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Badminton (D)":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:I{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.secondPlayerName, saved_data.secondPlayerMobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Carrom (S)":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Carrom (D)":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:I{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.secondPlayerName, saved_data.secondPlayerMobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Athletics":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Chess":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Kho-kho":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Dodgeball":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Throwball":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Table Tennis (S)":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
			
			elif saved_data.event == "Table Tennis (D)":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:I{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.secondPlayerName, saved_data.secondPlayerMobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
			
			
			elif saved_data.event == "Tug of War":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
			

			subject = "Successfully registered for SPoorthi!"
			message = f"Greetings From Spoorthi SPIT,\nHello {saved_data.fullName}, you have succesfully registered for {saved_data.event}.\nPlease Show this email at the time of Event.\nSee you at SPoorthi from 13-31st January'20.\nSports Team At SPIT"
			# from_email = settings.EMAIL_HOST_USER
			# mail = send_mail(subject, message, from_email, [request.POST['email']], fail_silently=False)
			messages.success(request, 'Your have been registerred successfuly!')
			return redirect('events')
	
	# if name == '*':
	return render(request, 'index.html', {'pageTitle':"Register"})
	# else:
	# 	return render(request, 'index.html')




def homePage(request):
	return render(request, 'home.html', {'pageTitle':"Home"})

def contact(request):
	return render(request, 'contact.html', {'pageTitle':"Contact"})



def gallery(request):
	data = {
		'glimpse': os.listdir(path='./static/images/glimpse'),
		'agility2021': os.listdir(path='./static/images/agility2021'),
		'pageTitle':"Gallery"
	}

	objects_SPoorthi = ImageModel.objects.filter(imageClass="SPoorthi").order_by('imageId')
	p_SPoorthi = Paginator(objects_SPoorthi, 2)
	page = request.GET.get('page1')
	try:
		objects_SPoorthi = p_SPoorthi.page(page)
	except:
		objects_SPoorthi = p_SPoorthi.page(1)

	objects_Agility = ImageModel.objects.filter(imageClass="Agility").order_by('imageId')
	p_Agility = Paginator(objects_Agility, 3)
	page = request.GET.get('page2')
	try:
		objects_Agility = p_Agility.page(page)
	except:
		objects_Agility = p_Agility.page(1)

	objects_Glimpse = ImageModel.objects.filter(imageClass="Glimpse").order_by('imageId')
	p_Glimpse = Paginator(objects_Glimpse, 4)
	page = request.GET.get('page3')
	try:
		objects_Glimpse = p_Glimpse.page(page)
	except:
		objects_Glimpse = p_Glimpse.page(1)
	
	data['spoorthi'] = objects_SPoorthi
	data['agility'] = objects_Agility
	data['glimpse'] = objects_Glimpse
	
	return render(request, 'gallery.html', data)




def eventPage(request, name=""):
	context = {}
	
	if name=="":
		allEvents = EventModel.objects.all()
		context['allEvents'] = allEvents
		context['pageTitle'] = "Events"
		return render(request, 'events.html', context)
	else:
		#get the event details by event name and add to context
		getEvent = EventModel.objects.get(eventName=name)
		context['item'] = getEvent
		context['pageTitle'] = "Event - "+name
		return render(request, 'event_details.html', context)