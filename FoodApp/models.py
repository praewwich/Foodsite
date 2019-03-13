from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
class Subscribe(models.Model):
    email = models.EmailField()
class Category(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Category = models.ForeignKey(Category,on_delete=None)
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    list_date = models.DateTimeField('date')
    image = models.ImageField(upload_to='FoodApp/static/ImageFood/%Y/%m/%d')
    is_public = models.BooleanField(default=True)
    def get_absolute_url(self):
        return f"/{self.Category}-{self.id}/"
    def __str__(self):
        return self.title



