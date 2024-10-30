from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User ,verbose_name=("profile"), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="profile-img/",blank=True,null=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True) 
    description = models.TextField(blank=True,null=True,max_length=500)
    fblink= models.URLField(blank=True,null=True, max_length=200)
    instlink= models.URLField(blank=True,null=True, max_length=200)
    twlink= models.URLField(blank=True,null=True, max_length=200)
    lilink= models.URLField(blank=True,null=True, max_length=200)
    is_team_member = models.BooleanField(default=False)
    role = models.CharField(max_length=50,default="User")
    def __str__(self):
        return f"{self.user.username}:Profile"

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)        

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, verbose_name=("reset_token"), on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()
    
    def is_expired(self):
        return  timezone.now() > self.expired_at

    