from django.db import models

class Accounts(models.Model):
    user = models.CharField(max_length = 50)
    account = models.CharField(max_length = 50)
    email = models.CharField(max_length=50)
    gender = (
        'Gender',(
            ('WOMAN','Woman'),('MAN','Man')
            )
        )
    phone = models.CharField(max_length = 50)
    group = models.CharField(max_length = 30)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return self.user


class Room(models.Model):
    rent_year = models.DateTimeField(auto_now_add=True, null=True)
    rent_month = models.IntegerField(null=True)
    monthly_fees = models.IntegerField()
    gas_fees =models.IntegerField()
    water_fees = models.IntegerField()
    elect_fees = models.IntegerField()

    def __str__(self):
        return self.monthly_fees

class Floor(models.Model):
    room = models.ForeignKey('Room', 
                            on_delete = models.CASCADE,)

    def __str__(self):
        return self.room

class Building(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 70)
    size = models.IntegerField()
    floor = models.ForeignKey('Floor',
                            on_delete = models.CASCADE,)

    def __str__(self):
        return self.name

