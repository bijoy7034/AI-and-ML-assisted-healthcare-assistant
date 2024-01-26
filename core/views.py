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
