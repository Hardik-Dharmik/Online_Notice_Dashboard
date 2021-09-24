from django.db import models
from django.contrib.auth.models import User
from Admin.models import addNotice

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Date_Of_Birth = models.DateField(auto_now=False)
    Roll_No = models.IntegerField(primary_key=False, null=False, unique=True)
    Department=models.CharField(max_length=100)
    Year_Of_Study=models.CharField(max_length=4)
    Gender=models.CharField(max_length=50)
    Admin_Status=models.BooleanField(default=False)
    # Notice=models.ForeignKey(addNotice,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

class Acknowledgment(models.Model):
    ack_id=models.AutoField(primary_key=True)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    notice=models.ForeignKey(addNotice,on_delete=models.CASCADE)
    is_acknowledged=models.BooleanField(default=False)
 
    def __str__(self):
        return f"{self.ack_id} Notice : {self.notice} to {self.profile}"