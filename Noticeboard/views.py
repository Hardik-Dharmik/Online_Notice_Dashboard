from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth import login,logout,authenticate
from user.models import Profile

def index(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'registration.html')


def viewprofile(request):
    return render(request, 'personal_details(user).html')


def __login__(request):
    if request.method == 'POST':
        choice=request.POST.get('flexRadioDefault','')
        loginusername=request.POST.get('username')
        loginpassword=request.POST.get('password')
        user=authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            profile=Profile.objects.filter(user=user)[0]

            if profile.Admin_Status==True:
                print("admin")
                login(request,user)
                # return render(request,'dashboard(admin).html',{'user':user})
                return redirect('dash_admin')

            else:
                print("user")
                login(request,user)
                # return render(request,'dashboard(user).html',{'user':user}).
                return redirect('dash_user')


        else:
            return HttpResponse("Wrong.")
    return render(request,'login.html')


def __logout__(request):
    logout(request)
    return render(request,'login.html')

def dash_user(request):
    return render(request,'dashboard(user).html',{'user':request.user})

def dash_admin(request):
    return render(request,'dashboard(admin).html',{'admin':request.user})
