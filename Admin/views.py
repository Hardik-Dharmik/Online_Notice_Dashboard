from django.shortcuts import render,redirect,HttpResponse
from user.models import Profile,Acknowledgment
from .models import addNotice

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
        # profiles=Profile.objects.filter(Department=dept)
        # for i in profiles:
        #     i.Notice=newNotice
        #     i.save()

        profiles=Profile.objects.filter(Department=dept)
        for profile in profiles:
            ack=Acknowledgment(profile=profile,notice=newNotice)
            ack.save()
        return render(request,'dashboard(admin).html')
    context={'user':request.user}
    return render(request,'add_notice.html',context)


def viewnotice(request):
    notices=addNotice.objects.all()
    print(notices)
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
        return redirect("notice")
    return HttpResponse("Bad Gateway")

def student(request):
    students=Profile.objects.filter(Admin_Status=False)
    print(students)
    context={'students':students,'admin':request.user}
    return render(request,'student(admin).html',context)