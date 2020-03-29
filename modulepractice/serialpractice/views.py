from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from serialblog.models import Task
from django.contrib.auth.models import User
from serialblog.api.serializers import TaskSerial # 1. making use of taskserial for
from django.http import JsonResponse

@api_view(['GET',])
def api_detail_view(request, id):
    try:
        task=TaskSerial.objects.get(id=id) # 2. passing it to 'task' object that we are passing in database
    except TaskSerial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    if request.method == "GET":
        serializer=TaskSerial(task) #task is input
        return JsonResponse(serializer.data) #serialized data



@api_view(['PUT',])
def api_update_view(request, id):
    try:
        task=TaskSerial.objects.get(id=id) # 2. passing it to 'task' object that we are passing in database
    except TaskSerial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    if request.method == "PUT":
        serializer=TaskSerial(task, data=request.data) #task is input
        data={} #think of it as context
        if serializer.is_valid():
            serializer.save()
            data["success"]="update successful" #just to tell user data saved
            return Response(data=data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE',])
def api_delete_view(request, id):
    try:
        task=TaskSerial.objects.get(id=id) # 2. passing it to 'task' object that we are passing in database
    except TaskSerial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    if request.method == "DELETE":
        operation = task.delete()
        data={}
        if operation:

             data["success"]="delete successful"
        else:
             data["failure"]="delete failed"
        return JsonResponse(data=data)

@api_view(['POST',])
def api_create_view(request):
    user=User.objects.get(pk=1)
    task= Task(author=user)
    if request.method == "POST":
        serializer= TaskSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.status.HTTP_400_BAD_REQUEST)
    

