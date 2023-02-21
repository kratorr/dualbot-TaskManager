from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Task, Tag

admin.site.register(User)
admin.site.register(Task)
admin.site.register(Tag)
