from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    last_login = models.DateTimeField(default=timezone.now)
    email = models.EmailField(primary_key=True)
    REQUIRED_FIELDS = ()
    USERNAME_FIELD = 'email'

    def is_authenticated(self):
        return True
