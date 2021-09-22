from django.shortcuts import HttpResponse,render,redirect

def index(request):
    return render(request,'login.html')
    
def register(request):
    return render(request,'registration.html')


    