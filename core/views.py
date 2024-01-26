from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Medical, User, Ment, Profile
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
import numpy as np
import os
from django.contrib import messages
import joblib as joblib
from django.contrib.auth.hashers import make_password


def home(request):
	return render(request, 'home.html')

def registerView(request):
	return render(request, 'register.html')

def registerUser(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password = make_password(password)

		a = User(username=username, email=email, password=password, is_patient=True)
		a.save()
		messages.success(request, 'Account Was Created Successfully')
		return redirect('reg')
	else:
		messages.error(request, 'Failed To Register, Try Again Later')
		return redirect('reg')

def loginView(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			if user.is_patient:
				return redirect('patient')
			elif user.is_doctor:
				return redirect('doctor')
			else:
				return redirect('login')
		else:
			messages.info(request, "Invalid Username Or Password")
			return redirect('login')
	else:
		return render(request, 'login.html')					


def patient_home(request):
	doctor = User.objects.filter(is_doctor=True).count()
	patient = User.objects.filter(is_patient=True).count()
	appointment = Ment.objects.filter(approved=True).count()
	medical1 = Medical.objects.filter(medicine='See Doctor').count()
	medical2 = Medical.objects.all().count()
	medical3 = int(medical2) - int(medical1)

	user_id = request.user.id
	user_profile = Profile.objects.filter(user_id=user_id)
	if not user_profile:
		context = {'profile_status':'Please Create Profile To Continue', 'doctor':doctor, 'ment':appointment, patient:'patient', 'drug':medical3}
		return render(request, 'patient/home.html', context)
	else:
		context = {'status':'1', 'doctor':doctor, 'ment':appointment, patient:'patient', 'drug':medical3}
		return render(request, 'patient/home.html', context)


def create_profile(request):
	if request.method == 'POST':
		birth_date = request.POST['birth_date']
		region = request.POST['region']
		country = request.POST['country']
		gender = request.POST['gender']
		user_id = request.user.id

		Profile.objects.filter(id = user_id).create(user_id=user_id, birth_date=birth_date, gender=gender, region=region)
		messages.success(request, 'Your Profile Was Created Successfully')
		return redirect('patient')
	else:
		user_id = request.user.id
		users = Profile.objects.filter(user_id=user_id)
		users = {'users':users}
		choice = ['1','0']
		gender = ["Male", "Female"]
		context = {"users": {"users":users}, "choice":{"choice":choice}, "gender":gender}
		return render(request, 'patient/create_profile.html', context)	



