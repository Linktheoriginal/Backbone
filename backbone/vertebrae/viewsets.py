from rest_framework import viewsets
from vertebrae.serializers import *

# ModelViewSet generates default views by expanding GenericAPIView with the Model Mixins
# http://www.django-rest-framework.org/api-guide/generic-views/#genericapiview
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class ToDoItemViewSet(viewsets.ModelViewSet):
	queryset = ToDoItem.objects.all()
	serializer_class = ToDoItemSerializer