from django.shortcuts import render
from user.models import Profile
from .models import addNotice

#For Viewing Profile of Admin
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
        return render(request,'dashboard(admin).html')
    context={'user':request.user}
    return render(request,'add_notice.html',context)


def viewnotice(request):
    notices=addNotice.objects.all()
    print(notices)
    context={'notices':notices}
    return render(request,'notice(admin).html',context)
