from django.contrib import admin
from .models import BlogAdmin
# Register your models here.

# class BlogAdminManager(admin.ModelAdmin):




admin.site.register(BlogAdmin)
