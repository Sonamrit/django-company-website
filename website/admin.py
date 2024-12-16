from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Setting)
class AdminSetting(admin.ModelAdmin):
    list_display =['name','slug','email','phone','address']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Page)
class AdminPage(admin.ModelAdmin):
    list_display =['title','slug','sub_title']
    prepopulated_fields = {'slug':('title',)}

@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display =['title','slug','sub_title']
    prepopulated_fields = {'slug':('title',)}

@admin.register(PageChild)
class AdminPageChild(admin.ModelAdmin):
    list_display =['page','sub_title']
    prepopulated_fields = {'slug':('title',)}

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display =['name']
    
@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display =['title','slug','sub_title']
    prepopulated_fields = {'slug':('title',)}
    
    