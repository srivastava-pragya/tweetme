from django.conf import settings
from django.db import models

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE,) #user.profile
	following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by',)
	#user.profile.following -- users I follow
	#user.profile.following -- user hat follow me
	def __str__(self):
		return str(self.following.all().count())