from django.contrib import admin
from blog.models import User, Task
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username','date_joined')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'taskName', 'taskDesc')