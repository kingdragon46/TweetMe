from django.db import models
from django.utils import timezone
from datetime import datetime, date
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    tweet_creation_date= models.DateTimeField(_("Date & Time"),default=timezone.now)