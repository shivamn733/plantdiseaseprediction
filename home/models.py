from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class contact(models.Model):
    #sno=models.CharField(max_length=15)
    name=models.CharField(max_length=15)
    phone=models.CharField(max_length=15)
    date=models.DateField()
    im=models.ImageField(upload_to="images")

    def __str__(self):
        return self.name
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verify=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

    
