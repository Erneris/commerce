from asyncio.windows_events import NULL
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)
    sbid = models.CharField(max_length = 10)
    img = models.TextField(default="https://media.istockphoto.com/photos/dotted-grid-paper-background-texture-seamless-repeat-pattern-picture-id1320330053?b=1&k=20&m=1320330053&s=170667a&w=0&h=XisfN35UnuxAVP_sjq3ujbFDyWPurSfSTYd-Ll09Ncc=")
    category = models.CharField(max_length = 20)
