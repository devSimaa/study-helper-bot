from django.contrib import admin

# Register your models here.
from .models import TodoList, Event



admin.site.register([TodoList, Event])
