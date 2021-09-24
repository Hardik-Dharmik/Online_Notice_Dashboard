from django.core.files.storage import FileSystemStorage
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):
    photo=models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to='photo', default='settings.MEDIA_ROOT/photo/anonymous.jpg')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Date_Of_Birth = models.DateField(auto_now=False)
    Roll_No = models.IntegerField(primary_key=False, null=False, unique=True)
    
    Department=models.CharField(max_length=100)
    Year_Of_Study=models.CharField(max_length=4)
    Gender=models.CharField(max_length=50)
    Admin_Status=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username