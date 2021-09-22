from django.shortcuts import render
from user.models import Profile

def viewprofile(request):
    user=Profile.objects.filter(user=request.user)[0]
    context={'user':user}
    return render(request,'personal_details(admin).html',context)

#For adding Notice
def addNotice(request):
    if request.method=='POST':
        title = request.POST['title'] 
        dept = request.POST['dept'] 
        content = request.POST['content'] 
        addNotice = AddNotice(title= title, dept = dept, content = content)
        addNotice.save()
        return render(request,'dashboard(admin).html')
    return render(request,'add_notice.html')
