from rest_framework import generics

from .models import Task, Tag
from .serializers import TaskSerializer, TagSerializer


class TaskList(generics.ListCreateAPIView):
    """ route: 'tasks/' """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """ route 'tasks/<int:pk>/ """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TagList(generics.ListCreateAPIView):
    """ route 'tags/' """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    """ route 'tags/<int:pk>/' """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

# How to make tasks by tag such as 'tasks/3/tags' for tasks with tag id 3
