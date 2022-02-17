from django.contrib import admin
from .models import Document, Folder, Topic



admin.site.register(Topic)
admin.site.register(Document)
admin.site.register(Folder)

# Register your models here.
