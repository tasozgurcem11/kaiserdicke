from django.db import models
from datetime import datetime

# Create your models here.
class SubscribedUser(models.Model):
    first_name = models.CharField(max_length=32, default='')
    last_name = models.CharField(max_length=32, default='')
    email = models.EmailField()
    telephonenummer = models.CharField( max_length=32, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email
        return self.created_at
