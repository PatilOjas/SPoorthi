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
	message = ""
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			saved_data = form.save()
			
			if saved_data.event == "Cricket":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
				message = f"Greetings From Spoorthi SPIT,\n\nHello {saved_data.fullName}, you have successfully registered for {saved_data.event}.The captain of the team is supposed to enter the team details in the link provided below.\n\nTeam: https://forms.gle/j5TZKuzn7CkAkhQD9\n\nPlease Show this email at the time of Event.\nSee you at SPoorthi from 15th Feb'22-3rd Mar'22.\nSports Team At SPIT"
			
			elif saved_data.event == "Football":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
				message = f"Greetings From Spoorthi SPIT,\n\nHello {saved_data.fullName}, you have successfully registered for {saved_data.event}.\n\nThe captain of the team is supposed to enter the team details in the appropriate links provided below.\nBoys:https://forms.gle/zm2QpcKxszmuqxPi8 \nGirls: https://forms.gle/6Nx8kPad7R2ExT1H9\n\nPlease Show this email at the time of Event.\nSee you at SPoorthi from 15th Feb'22-3rd Mar'22.\nSports Team At SPIT"
			
			elif saved_data.event == "Volleyball":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
				message = f"Greetings From Spoorthi SPIT,\n\nHello {saved_data.fullName}, you have successfully registered for {saved_data.event}.\n\nThe captain of the team is supposed to enter the team details in the link provided below.\n\nTeam: https://forms.gle/F341jRPXbHw8gXGh6\n\nPlease Show this email at the time of Event.\nSee you at SPoorthi from 15th Feb'22-3rd Mar'22.\nSports Team At SPIT"
			
			elif saved_data.event == "Badminton (S)":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
				message = f"Greetings From Spoorthi SPIT,\n\nHello {saved_data.fullName}, you have successfully registered for {saved_data.event}.\nPlease Show this email at the time of Event.\nSee you at SPoorthi from 15th Feb'22-3rd Mar'22.\nSports Team At SPIT"
			
			elif saved_data.event == "Badminton (D)":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:I{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.secondPlayerName, saved_data.secondPlayerMobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
				message = f"Greetings From Spoorthi SPIT,\n\nHello {saved_data.fullName}, you and {saved_data.secondPlayerName} have successfully registered for {saved_data.event}.\nPlease Show this email at the time of Event.\nSee you at SPoorthi from 15th Feb'22-3rd Mar'22.\nSports Team At SPIT"
			
			elif saved_data.event == "Carrom (S)":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
				message = f"Greetings From Spoorthi SPIT,\n\nHello {saved_data.fullName}, you have successfully registered for {saved_data.event}.\nPlease Show this email at the time of Event.\nSee you at SPoorthi from 15th Feb'22-3rd Mar'22.\nSports Team At SPIT"
			
			elif saved_data.event == "Carrom (D)":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:I{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.secondPlayerName, saved_data.secondPlayerMobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
				message = f"Greetings From Spoorthi SPIT,\n\nHello {saved_data.fullName}, you and {saved_data.secondPlayerName} have successfully registered for {saved_data.event}.\nPlease Show this email at the time of Event.\nSee you at SPoorthi from 15th Feb'22-3rd Mar'22.\nSports Team At SPIT"
			
			elif saved_data.event == "Kabaddi":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
				message = f"Greetings From Spoorthi SPIT,\n\nHello {saved_data.fullName}, you have successfully registered for {saved_data.event}.\n\nThe captain of the team is supposed to enter the team details in the link provided below.\n\nTeam: https://forms.gle/PW74hdqqWxdaLxXf6\n\nPlease Show this email at the time of Event.\nSee you at SPoorthi from 15th Feb'22-3rd Mar'22.\nSports Team At SPIT"
			
			elif saved_data.event == "Chess":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
				message = f"Greetings From Spoorthi SPIT,\n\nHello {saved_data.fullName}, you have successfully registered for {saved_data.event}.\nPlease Show this email at the time of Event.\nSee you at SPoorthi from 15th Feb'22-3rd Mar'22.\nSports Team At SPIT"
			
			elif saved_data.event == "Kho-kho":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
				message = f"Greetings From Spoorthi SPIT,\n\nHello {saved_data.fullName}, you have successfully registered for {saved_data.event}.\n\nThe captain of the team is supposed to enter the team details in the link provided below.\n\nTeam: https://forms.gle/uSXZy1F4MXY8Zmwx9 \n\nShow this email at the time of Event.\nSee you at SPoorthi from 15th Feb'22-3rd Mar'22.\nSports Team At SPIT"
			
			elif saved_data.event == "Dodgeball":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
				message = f"Greetings From Spoorthi SPIT,\n\nHello {saved_data.fullName}, you have successfully registered for {saved_data.event}.\n\nThe captain of the team is supposed to enter the team details in the link provided below.\nTeam: https://forms.gle/DxMaFXiMzWrdA578A \n\nShow this email at the time of Event.\nSee you at SPoorthi from 15th Feb'22-3rd Mar'22.\nSports Team At SPIT"
			
			elif saved_data.event == "Throwball":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
				message = f"Greetings From Spoorthi SPIT,\n\nHello {saved_data.fullName}, you have successfully registered for {saved_data.event}.\n\nThe captain of the team is supposed to enter the team details in the link provided below.\n\nTeam: https://forms.gle/X1sJb4qhUG7mMKDo6 \n\nShow this email at the time of Event.\nSee you at SPoorthi from 15th Feb'22-3rd Mar'22.\nSports Team At SPIT"
			
			elif saved_data.event == "Table Tennis":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
				message = f"Greetings From Spoorthi SPIT,\n\nHello {saved_data.fullName}, you have successfully registered for {saved_data.event}.\nPlease Show this email at the time of Event.\nSee you at SPoorthi from 15th Feb'22-3rd Mar'22.\nSports Team At SPIT"
			
			elif saved_data.event == "Tug of War":
				sh = SheetEditor(sheetName=sheet_name, sheet=saved_data.event)
				sh.wks.update(f"A{len(sh.wks.get_all_records()) + offset}:G{len(sh.wks.get_all_records()) + offset}", [[saved_data.playerId, saved_data.email, saved_data.fullName, saved_data.mobNo, saved_data.collegeName, saved_data.event, str(saved_data.datetimestamp)]])
				message = f"Greetings From Spoorthi SPIT,\n\nHello {saved_data.fullName}, you have successfully registered for {saved_data.event}.\n\nThe captain of the team is supposed to enter the team details in the link provided below.\n\nTeam: https://forms.gle/wRDpQGRRk375nhr78 \n\nShow this email at the time of Event.\nSee you at SPoorthi from 15th Feb'22-3rd Mar'22.\nSports Team At SPIT"
			

			subject = "Successfully registered for SPoorthi!"
			from_email = settings.EMAIL_HOST_USER
			send_mail(subject, message, from_email, [request.POST['email']], fail_silently=False)

			messages.success(request, 'Your have been registerred successfuly!')
			
			return redirect('events')
	
	return render(request, 'index.html', {'pageTitle':"Register"})
	
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
	
	objects_Agility = ImageModel.objects.filter(imageClass="Agility").order_by('imageId')
	
	objects_Glimpse = ImageModel.objects.filter(imageClass="Glimpse").order_by('imageId')
	
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
		getEvent = EventModel.objects.get(eventName=name)
		context['item'] = getEvent
		context['pageTitle'] = "Event - "+name
		return render(request, 'event_details.html', context)