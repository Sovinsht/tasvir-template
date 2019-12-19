from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import PhotoModel,CommentModel
from .forms import PhotoForm

# Create your views here.
def index(request):
    if 'id' in request.session:
        upload = PhotoModel.objects.all()
        comments = CommentModel.objects.all()
        return render(request, 'photo_app/index.html',{'upload': upload, 'comments': comments})
    else:
        return redirect('user:login')

def add(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES) 
        if form.is_valid():
            try:
                form.save()
                return redirect('photo_app:index')
            except Exception as e:
                print(form.errors)
                print(e)
                # return redirect('photo_app:index')
                return HttpResponse('failed')    
        else:
            print(form.errors)
            return HttpResponse('Form is not valid')    
    else:
        form = PhotoForm
        return render(request,"photo_app/addphoto.html",{'form':form})

def edit(request,id):
    photo = PhotoModel.objects.get(id=id)

    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES, instance=photo) 
        if form.is_valid():
            try:
                form.save()
                return redirect('photo_app:index')
            except Exception as e:
                print(form.errors)
                print(e)
                # return redirect('photo_app:index')
                return HttpResponse('failed')    
        else:
            print(form.errors)
            return HttpResponse('Form is not valid')    
    else:
       # form = PhotoForm
        return render(request,"photo_app/editphoto.html",{'photo':photo})

