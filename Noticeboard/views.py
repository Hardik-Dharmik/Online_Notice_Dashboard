from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth import login,logout,authenticate
from user.models import Profile,Acknowledgment
from Admin.models import addNotice
from django.contrib import messages


def index(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'registration.html')


def viewprofile(request):
    return render(request, 'personal_details(user).html')


def __login__(request):
    if request.method == 'POST':
        loginusername=request.POST.get('username')
        loginpassword=request.POST.get('password')
        user=authenticate(username=loginusername,password=loginpassword)
        print(user)
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
            messages.error(request,'User with these details not found, kindly retry')    
    return render(request,'login.html')


def __logout__(request):
    logout(request)
    return render(request,'login.html')

def dash_user(request):
    profile=Profile.objects.filter(user=request.user)[0]
    acks=Acknowledgment.objects.filter(profile=profile,is_acknowledged=False)
    # print(profile.Department,profile.Year_Of_Study)
    notices=[]
    for i in acks:
        print(i.notice)
        notices.append(i.notice)
    # notices=list_to_queryset(notices)
    print(notices)
    # if profile.Department=="ALL":
    #     notices=addNotice.objects.all(year=profile.Year_Of_Study)
    # else:
    #     notices=addNotice.objects.filter(dept=profile.Department,year=profile.Year_Of_Study)
    print("notices=",notices)
    context={'user':request.user,'notices':notices,'acks':acks}
    return render(request,'dashboard(user).html',context)

def dash_admin(request):
    user=request.user
    print(user)
    messages.success(request, f"Welcome {user}")
    return render(request,'dashboard(admin).html',{'admin':request.user})
    
def notice(request):
    notices=addNotice.objects.all()
    context={'notices':notices,'admin':request.user}
    return render(request,'notice(admin).html',context)

def addnotice(request):
    return render(request,'add_notice.html',{'admin':request.user})

def student(request):
    students=Profile.objects.filter(Admin_Status=False)
    print(students)
    context={'students':students,'admin':request.user}
    return render(request,'student(admin).html',context)

