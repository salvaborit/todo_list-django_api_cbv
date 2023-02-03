from django.urls import path
from .views import TaskList, TaskDetail, TasksByTagList
from .views import TagList, TagDetail

urlpatterns = [
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:pk>', TaskDetail.as_view()),

    path('tags/', TagList.as_view()),
    path('tags/<int:pk>/', TagDetail.as_view()),

    path('tasks/<int:tag_pk>/tags/', TasksByTagList.as_view()),
]
