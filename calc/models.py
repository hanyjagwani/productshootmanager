from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Design(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    img=models.FileField(upload_to='img/')
    description=models.CharField(max_length=100)
    price=models.IntegerField()
    
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    user_type=models.CharField(max_length=10)
    contact=models.IntegerField()
    address=models.CharField(max_length=200)
    
class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    # quantity=models.IntegerField()
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)