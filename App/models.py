from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Records(models.Model):
    user=models.ForeignKey(User,related_name='records',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)


    def __str__(self):
        return self.first_name 
