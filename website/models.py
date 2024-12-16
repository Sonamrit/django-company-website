from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.
class Setting(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=100)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=100, blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    descripton = models.TextField(blank=True,null=True)
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    favicon = models.ImageField(upload_to='favicon/', blank=True,null=True)
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_decription = models.TextField( blank=True, null=True)
    meta_keyword = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.name


class Page(models.Model):
    title  = models.CharField(max_length=100) 
    slug = models.SlugField(max_length=100, unique=100)
    sub_title = models.CharField(max_length=100, blank=True , null=True)
    image = models.ImageField(upload_to='page/',blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    description = CKEditor5Field(blank=True, null=True)
    meta_title = models.CharField(max_length=100, blank=True , null=True)
    meta_decription = models.TextField( blank=True, null=True)
    meta_keyword = models.TextField(blank=True, null=True)
    page_section_name = models.CharField(max_length=100,blank=True , null=True)


class Service(models.Model):
    title  = models.CharField(max_length=100) 
    slug = models.SlugField(max_length=100, unique=100)
    sub_title = models.CharField(max_length=100, blank=True , null=True)
    image = models.ImageField(upload_to='page/',blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    description = CKEditor5Field(blank=True, null=True)
    meta_title = models.CharField(max_length=100, blank=True , null=True)
    meta_decription = models.TextField( blank=True, null=True)
    meta_keyword = models.TextField(blank=True, null=True)

    @property
    def get_limit_summary(self):
        return self.summary[:100]+'...'


class PageChild(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    title  = models.CharField(max_length=100) 
    slug = models.SlugField(max_length=100, unique=100)
    sub_title = models.CharField(max_length=100, blank=True , null=True)
    image = models.ImageField(upload_to='page/',blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    description = CKEditor5Field(blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title  = models.CharField(max_length=100) 
    slug = models.SlugField(max_length=100, unique=100)
    sub_title = models.CharField(max_length=100, blank=True , null=True)
    image = models.ImageField(upload_to='page/',blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    description = CKEditor5Field(blank=True, null=True)
    meta_title = models.CharField(max_length=100, blank=True , null=True)
    meta_decription = models.TextField( blank=True, null=True)
    meta_keyword = models.TextField(blank=True, null=True)

    @property
    def get_limit_summary(self):
        return self.summary[:150]+'...'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
      