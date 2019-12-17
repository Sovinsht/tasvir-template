from django.shortcuts import render



from django.http import HttpResponse

def display(request):
    
    return render(request, 'user_app/index.html')