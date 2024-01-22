from rest_framework import serializers
from .modals import Drink

class Drinkserilizer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id','name','description']