from pydoc_data.topics import topics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import DocumentSerializer, FolderSerializer, TopicSerializer, DocumentNameSerializer
from .models import Document, Folder, Topic
from django_filters.rest_framework import DjangoFilterBackend

#from rest_framework.decorators import detail_route

# Create your views here.
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all().order_by('-id')
    serializer_class = DocumentSerializer

class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class DocumentsInFolderViewSet(viewsets.ReadOnlyModelViewSet ):
  
    serializer_class = DocumentNameSerializer
    queryset = Document.objects.all()    

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['folder_id']

class DocumentsOfTopicViewSet(viewsets.ReadOnlyModelViewSet ):
  
    serializer_class = DocumentNameSerializer
    queryset = Document.objects.all()    

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['topic__id']

class DocumentInFolderOfTopicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Document.objects.all()#filter(topics__topic_name__contains="SpekiLove" , folder__folder_name__contains="s")
    serializer_class = DocumentNameSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['topic__topic_name', 'folder__folder_name']
#http://naseem.com/search/?topics__topic_name=SpekiLove!&folder__folder_name=Customer Feedback
