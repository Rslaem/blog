from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='userprofile')
    birth = models.DateField(blank=True,null=True)
    avatar = models.CharField(max_length=200,blank=True)
    email = models.EmailField(blank=True)
    bio = models.TextField(blank=True)
    def __str__(self):
        return 'user {}'.format(self.user.username)
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.userprofile.save()
# Create your models here.
