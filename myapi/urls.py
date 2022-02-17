from posixpath import basename
from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'folders',views.FolderViewSet)
router.register(r'topics', views.TopicViewSet)
router.register(r'documents',views.DocumentViewSet)
router.register(r'list-documents-in-folderid', views.DocumentsInFolderViewSet, basename='documents-in-folder')
router.register(r'list-documents-of-topicid', views.DocumentsOfTopicViewSet, basename='documents-by-topics')
router.register(r'search', views.DocumentInFolderOfTopicViewSet, basename='documents-in-folder-by-topics')


urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
   
]
