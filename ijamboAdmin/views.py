from django.shortcuts import render
from django.contrib.auth.models import User
from ijambo.models import *
# Create your views here.

def home(request):
	profile = Profil.objects.get(user=request.user)
	return render(request, 'index2.html', locals())