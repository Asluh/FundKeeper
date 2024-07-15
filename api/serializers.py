from rest_framework import serializers

from django.contrib.auth.models import User

from api.models import Expence,Income



class Userserializer(serializers.ModelSerializer):
 
    class Meta:
 
        model=User
 
        fields=['id','username','password','email','first_name','last_name']
 
        read_only_fields=['id']

    def create(self, validated_data):
 
        return User.objects.create_user(**validated_data)

    
class  ExpenceSerializer(serializers.ModelSerializer):

    owner=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Expence

        fields="__all__"

        read_only_fields=['id','owner','created_date','updated_date','is_active']

class IncomeSerializer(serializers.ModelSerializer):

    owner=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Income

        fields="__all__"
        
        read_only_fields=['id','owner','created_date','updated_date']

