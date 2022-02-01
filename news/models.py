from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Setting(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logo')
    meta_title = models.CharField(max_length=255)
    meta_keyword = models.TextField()
    meta_description = models.TextField()
    description = RichTextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    cat_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.cat_name


class Blog(models.Model):
    cat_id = models.ForeignKey(Category, models.PROTECT)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    meta_title = models.CharField(max_length=255)
    meta_keyword = models.TextField()
    meta_description = models.TextField()
    image = models.ImageField(upload_to='blog')
    page_visit = models.IntegerField(default=0)
    description = RichTextField()

    def __str__(self):
        return self.title
