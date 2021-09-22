from django.shortcuts import render
from user.models import Profile
from Admin.models import addNotice

def viewprofile(request):
    user=Profile.objects.filter(user=request.user)[0]
    context={'user':user}
    return render(request,'personal_details(admin).html',context)

#For adding Notice
def addNotice(request):
    if request.method=='POST':
        title_notice = request.POST['title_notice'] 
        dept = request.POST['dept'] 
        content = request.POST['content'] 
        AddNotice = addNotice(title_notice = title_notice, dept = dept, content = content)
        AddNotice.save()
        return render(request,'dashboard(admin).html')
    return render(request,'add_notice.html')
