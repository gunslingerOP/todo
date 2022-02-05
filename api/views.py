from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Task
from .serializer import *

@api_view(['GET', 'POST'])
def tasks_list(request):
    if request.method == 'GET':
        data = Task.active.all()

        serializer =TaskSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.is_active = False
        task.save(update_fields=['is_active'])
        return Response(status=status.HTTP_204_NO_CONTENT)