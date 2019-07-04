from rest_framework import serializers 
from .models import Accounts 

class AccountsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Accounts
        fields = ('user','password','account',
                'gender','phone','group') 

class RoomSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Room
        fields = ('rent_year','rent_month','monthly_fees', 'gas_fees',
                'water_fees', 'elect_fees') 

class BuildingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Building
        fields = ('name','address','size','floor') 


