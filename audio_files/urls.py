from django.conf.urls import url
from django.urls import path, include
from .views import FilesListApiView, FileDetailApiView


urlpatterns = [
    path('<str:file_type>/', FilesListApiView.as_view()),
    path('<str:file_type>/<int:file_id>/', FileDetailApiView.as_view()),
]