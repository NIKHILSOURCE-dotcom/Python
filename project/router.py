
from rest_framework import routers

from appexample.viewsets import Userviewset
from appexample.serializers import *

router = routers.DefaultRouter()
router.register('User',Userviewset)