from django.shortcuts import render
from django.http import HttpResponse
from .models import PhotoModel,CommentModel

# Create your views here.
def index(request):
    
    upload = PhotoModel.objects.all()
    comments = CommentModel.objects.all()
    return render(request, 'photo_app/index.html',{'upload': upload, 'comments': comments})