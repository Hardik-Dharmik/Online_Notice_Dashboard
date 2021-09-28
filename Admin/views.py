from django.shortcuts import render,redirect,HttpResponse
from user.models import Profile,Acknowledgment
from .models import addNotice
from django.contrib.auth.models import User
from django.contrib import messages

def viewprofile(request):
    user=Profile.objects.filter(user=request.user)[0]
    context={'user':user}
    return render(request,'personal_details(admin).html',context)

#For adding Notice
def __addNotice__(request):
    if request.method=='POST':
        title_notice = request.POST['title_notice'] 
        dept = request.POST['dept'] 
        content = request.POST['content'] 
        newNotice = addNotice(title_notice= title_notice, dept = dept, content = content)
        newNotice.save()

        profile=None
        if dept=="ALL":
            profiles=Profile.objects.filter(Admin_Status=False)
        else:
            profiles=Profile.objects.filter(Department=dept)

        for profile in profiles:
            ack=Acknowledgment(profile=profile,notice=newNotice)
            ack.save()
        messages.success(request,'Notice added!')
        return redirect('show notice')
    context={'user':request.user}
    return render(request,'add_notice.html',context)


def viewnotice(request):
    notices=addNotice.objects.all()
    context={'notices':notices}
    return render(request,'notice(admin).html',context)

def updatenotice(request):
    if request.method=='POST':
        noticeid=request.POST.get('noticeid')
        notice=addNotice.objects.filter(sno=noticeid)[0]
        context={'notice':notice}
        return render(request,"update_notice.html",context)
    return redirect("notice")

def updatenotice_in_db(request):
    if request.method=='POST':
        noticeid=request.POST.get('noticeid')
        title=request.POST.get('title_notice')
        content=request.POST.get('content')
        dept=request.POST.get('dept')
        notice=addNotice.objects.filter(sno=noticeid)[0]
        print(" before update: ",notice)

        notice.title_notice=title
        notice.dept=dept
        notice.content=content
        notice.save()
        print(" after update: ",notice)
        context={'notice':notice}
        return redirect("notice")
    return redirect("notice")

def deletenotice(request):
    if request.method=='POST':
        noticeid=request.POST.get('noticeid')
        notice=addNotice.objects.filter(sno=noticeid).first()
        notice.delete()
        messages.error(request,'Notice deleted Sucessfully!')
        return redirect("notice")
    return HttpResponse("Bad Gateway")

def student(request):
    students=Profile.objects.filter(Admin_Status=False)
    print(students)
    context={'students':students,'admin':request.user}
    return render(request,'student(admin).html',context)

def viewinfo(request,sno):
    notice=addNotice.objects.filter(sno=sno).first()
    print(notice)
    acks=None

    acks=Acknowledgment.objects.filter(notice=notice)
    print(acks)
    viewed=[]
    notviewed=[]
    for i in acks:
        if i.is_acknowledged==True:
            viewed.append(i)
        else:
            notviewed.append(i)

    context={'viewed':viewed,'notviewed':notviewed,'notice':notice}
    return render(request,'notice_info.html',context)

def viewstudent(request,username):
    user=User.objects.filter(username=username).first()
    print(user)
    profile=Profile.objects.filter(user=user).first()
    context={'profile':profile}
    return render(request,"personal_details(user).html",context)

def deletestudent(request,username):
    user=User.objects.filter(username=username).first()
    user.delete()
    messages.success(request,f"User {user} deleted successfully!!")
    return redirect("student")

user1=None
def updatestudent(request,username):
    user=User.objects.filter(username=username).first()
    user1=user
    print("User inside 1",user1)
    profile=Profile.objects.filter(user=user).first()
    context={'profile':profile}
    return render(request,'update_user.html',context)

def updatestudent_indb(request):
        if request.method=='POST':
            orgname=request.POST.get("orgname")
            photo=request.POST.get("fileupload")
            fname=request.POST.get("fname")
            username=request.POST.get("username")
            dob=request.POST.get("dob")
            rollno=request.POST.get("rollno")
            email=request.POST.get("email")
            password=request.POST.get("password")
            cpassword=request.POST.get("cpassword")
            dept=request.POST.get("dept")
            yos=request.POST.get("yos")
            male=request.POST.get("male","off")
            female=request.POST.get("female","off")
            pnts=request.POST.get("pnts","off")
            gender=""
            if male=="on": 
                gender="Male"
            elif female=="on":
                gender="Female"
            else:
                gender="Prefer Not to say"
            print("User inside 1",user1)
            user=User.objects.filter(username=orgname).first()
            profile=Profile.objects.filter(user=user).first()
            user.username=username
            user.email=email
            user.password=password

            user.save()
            print("Inside update")
            profile.photo=photo
            profile.Date_Of_Birth=dob
            profile.Roll_No=rollno
            profile.Department=dept
            profile.Year_Of_Study=yos
            profile.Gender=gender
            profile.save()
            messages.success(request,"Profile updated successfully")

            return redirect("student")