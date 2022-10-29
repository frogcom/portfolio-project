from django.shortcuts import render, redirect, get_object_or_404
from .models import Socials

# Create your views here.

def home(request):
 Socials = Socials.objects
 return render(request, 'socials/socials.html', {'socials': Socials})

def detail(request, socials_id):
 Socials = get_object_or_404(Socials, pk=socials_id)
 return render(request, '/detail.html', {'socials': Socials})
