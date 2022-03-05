from .import models
from .import serializers


from rest_framework import viewsets


class Userviewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.Userserializers
