from asyncio.windows_events import NULL
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)
    sbid = models.CharField(max_length = 10)
    img = models.CharField(max_length = 10000, null=True, blank=True, default=None)