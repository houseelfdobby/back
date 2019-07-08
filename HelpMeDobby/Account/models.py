from django.db import models
from django.contrib.auth.models import User

class Accounts(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    account = models.CharField(max_length = 50)
    email = models.CharField(max_length=50)
    gender = (
        'Gender',(
            ('WOMAN','Woman'),('MAN','Man')
            )
        )
    phone = models.CharField(max_length = 50)
    group = models.CharField(max_length = 30)


    def __str__(self):
        return self.user