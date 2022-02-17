
from rest_framework import serializers

from .models import Document, Folder, Topic

class TopicSerializer(serializers.ModelSerializer):
    topic_id = serializers.IntegerField(read_only=True, source="id")
    class Meta:
        model = Topic
        fields = ('topic_id', 'topic_name')

class FolderSerializer(serializers.ModelSerializer):
    folder_id = serializers.IntegerField(read_only=True, source="id")
    class Meta:
        model = Folder
        fields = ('folder_id', 'folder_name','folder_short_description')

class DocumentSerializer(serializers.ModelSerializer):
    document_id = serializers.IntegerField(read_only=True, source="id")
    class Meta:
        model = Document
        fields = ("document_id","document_name","document_short_description","folder","topic")#'__all__'        

class DocumentNameSerializer(serializers.ModelSerializer):
    document_id = serializers.IntegerField(read_only=True, source="id")
    document_topics  = TopicSerializer(many=True, required=False, source="topic")
    folder = FolderSerializer()
    class Meta:
        model = Document
        fields = ('document_id', 'document_name', 'document_topics', 'document_short_description', 'folder')#'__all__'
 