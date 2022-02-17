from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=60, unique=True)
   
    def __str__(self):
        return self.topic_name
        
class Folder(models.Model):
    folder_name = models.CharField(max_length=60, unique=True)
    #topics = models.ManyToManyField(Topic, related_name="folders") 
    folder_short_description = models.CharField(max_length=140)     
    
    def __str__(self):
        return self.folder_name

class Document(models.Model):
    document_name = models.CharField(max_length=60)
    document_short_description = models.CharField(max_length=140)   
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    topic = models.ManyToManyField(Topic, related_name="documents") 
    
    def __str__(self):
        return self.document_name