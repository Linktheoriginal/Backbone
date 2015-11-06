from django.contrib.auth.models import User, Group
from rest_framework import serializers
from vertebrae.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		#have to add this extra_kwargs line to make it go to the vertebrae namespace,
		#because I had to get all fancy and want to put the API at the /backbone app level and not at root /.
		#https://github.com/tomchristie/django-rest-framework/issues/2760
		extra_kwargs = {'url': {'view_name': 'vertebrae:user-detail'}}
		model = User
		fields = ('url', 'username', 'email', 'is_staff', 'groups', 'id')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		extra_kwargs = {'url': {'view_name': 'vertebrae:group-detail'}}
		model = Group
		fields = ('url', 'name', 'id')

class ToDoItemSerializer(serializers.HyperlinkedModelSerializer):
	#if you override validation on the field, then you have to recreate ALL the validation
	#by default it will apply the validation on the model - I've added a min_length and custom error messages
	title = serializers.CharField(min_length=4, max_length=200, error_messages={'max_length':'way too long, bud', 'min_length':'if it ain\'t four letters, it ain\'t worth doin\''})

	class Meta:
		extra_kwargs = {'url': {'view_name': 'vertebrae:todoitem-detail'}}
		model = ToDoItem
		fields = ('url', 'title', 'completed', 'id')