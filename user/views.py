from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import Profile, Acknowledgment
from Admin.models import addNotice
from django.core.files.storage import FileSystemStorage


# Create your views here.
def index(request):
    return HttpResponse("Inside user")


def register(request):
    if request.method == 'POST':
        user_image = request.FILES["fileupload"]
        fss = FileSystemStorage()
        file = fss.save(user_image.name, user_image)
        file_url = fss.url(file)
        fname = request.POST.get("fname")
        username = request.POST.get("username")
        dob = request.POST.get("dob")
        rollno = request.POST.get("rollno")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        dept = request.POST.get("dept")
        yos = request.POST.get("yos")
        male = request.POST.get("male", "off")
        female = request.POST.get("female", "off")
        pnts = request.POST.get("pnts", "off")
        gender = ""
        if male == "on":
            gender = "Male"
        elif female == "on":
            gender = "Female"
        else:
            gender = "Prefer Not to say"

        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = fname
        new_user.save()

        newprofile = Profile(image=user_image, user=new_user, Date_Of_Birth=dob,
                             Roll_No=rollno, Department=dept, Year_Of_Study=yos, Gender=gender)
        newprofile.save()
        return render(request, 'login.html')

    return render(request, 'registration.html')


def viewprofile(request):
    user = Profile.objects.filter(user=request.user)[0]
    print(user.Gender)
    context = {'profile': user}
    return render(request, 'personal_details(user).html', context)


def dash(request):
    profile = Profile.objects.filter(user=request.user)[0]
    notices = addNotice.objects.filter(dept=profile.Department, year=profile.Year_Of_Study)
    print(notices)
    return render(request, 'dashboard(user).html')


def acknow(request):
    if request.method == 'POST':
        id = request.POST.get('ackid')
        obj = Acknowledgment.objects.filter(ack_id=id).first()
        obj.is_acknowledged = True
        obj.save()
        return redirect("dash_user")

    else:
        return HttpResponse("Bad Gateway")
