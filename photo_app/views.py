from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import PhotoModel,CommentModel
from .forms import PhotoForm, CommentForm
from user_app.models import UserModel

# Create your views here.
def index(request):
    if 'id' in request.session:
        upload = PhotoModel.objects.all()
        comments = CommentModel.objects.all()[:20]
        return render(request, 'photo_app/index.html',{'upload': upload, 'comments': comments})
    else:
        return redirect('user:login')

def profile(request):
    if 'id' in request.session:
        user_id = request.session['id']
        upload = PhotoModel.objects.filter(uploaded_by=user_id)
        user = UserModel.objects.get(id = user_id)
        dict = {'upload':upload, 'user':user}
        return render(request, 'photo_app/profile.html',dict)
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
    user = UserModel.objects.get(id=id)
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES, instance=photo) 
        form1 = UserModel(request.POST, request.FILES, instance=user)
        if form1.is_valid() and form.is_valid():
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
        return render(request,"photo_app/edit-profile.html",{'photo':photo, 'user':user})

def edit1(request,id):
    comment = CommentModel.objects.all()

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, instance=comment) 
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
        return render(request,"photo_app/editcomment.html",{'comment':comment})

def delete(request, id):
    photo = PhotoModel.objects.get(id=id)
    photo.delete()
    return redirect('photo_app:profile')

def search(request):
    if 'id' not in request.session:
        return redirect('user:login')

    userid = request.session.get('id',None)

    if request.method == 'GET':
        query = request.GET.get('q',None)
        if query:
            d = {
                    'profiles' : UserModel.objects.filter(user_name__icontains=query).exclude(id=userid),
                    'query' : query
                }    
            return render(request,'photo_app/search_result.html',d)
        else:
                return redirect('photo_app:index')
    else:
            return redirect('photo_app:index')
