from rest_framework import serializers
from serialpractice.models import TaskPract

class TaskSerial(serializers.ModelSerializer):
    class Meta:
        model=TaskPract
        fields=['name']


        #model serializer capability of giving off all the queryobjects of model set
        #create, modify
