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
