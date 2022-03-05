from rest_framework import serializers
from appexample.models import User





class Userserializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
    
