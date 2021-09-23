from django.db import models

# Create your models here.
# Database ----> Excel workbook

class addNotice(models.Model):
    sno = models.AutoField(primary_key=True)
    title_notice = models.CharField(max_length=255)
    dept = models.CharField(max_length=10)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Title is '+self.title_notice
    
