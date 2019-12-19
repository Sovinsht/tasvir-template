from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import UserModel

def display(request):
    
    return render(request, 'user_app/index.html')

def loginauth(request):
    if request.method == "POST":
        e = request.POST.get('email')
        p = request.POST.get('pass')

        user = UserModel.objects.filter(email=e, password = p)

        if(user.count() > 0):
            for user in user:
                request.session['email'] = user.email
                request.session['id'] = user.id
                request.session['username'] = user.user_name

                return redirect('photo_app:index')
        else:
            return HttpResponse('Wrong Email or Password')


    else:
        return render(request, 'user_app\login.html')

def logout(request):
        request.session.flush()
        return redirect('user:login')