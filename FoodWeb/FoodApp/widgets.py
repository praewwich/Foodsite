from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorUploadingWidget
from FoodApp.models import Post

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

