from django.contrib import admin  # type: ignore
from .models import Topic
from .models import Entry

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)