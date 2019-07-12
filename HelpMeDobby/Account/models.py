from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, user_name, account, zip_code, address, layer , room_num, password=None):
 
        user = self.model(
            user_name = user_name,
            account = account,
            zip_code = zip_code,
            address = address,
            layer = layer,
            room_num = room_num,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, account, zip_code, address, layer , room_num, password):
        user = self.create_user(
            user_name = user_name,
            password=password,
            account = account,
            zip_code = zip_code,
            address = address,
            layer = layer,
            room_num = room_num,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_name = models.CharField(max_length = 20 , unique=True)
    account = models.CharField(max_length = 50)
    zip_code = models.CharField(max_length = 10)
    address = models.CharField(max_length = 50)
    layer = models.CharField(max_length=10)
    room_num=models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['account','zip_code','address','layer','room_num']

    def __str__(self):
        return self.user_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin