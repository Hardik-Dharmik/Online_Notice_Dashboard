from django.shortcuts import render,HttpResponse
from Admin.models import addNotice 
# Create your views here.


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