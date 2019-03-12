from django import forms
from .models import Post,Subscribe
from django.contrib.auth.forms import AuthenticationForm

class PostForm(forms.ModelForm):
    list_date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        fields = ['id','user','Category','title','content','list_date','is_public']
        
class UploadFileForm(forms.Form):
    file = forms.FileField()

class SubscribeEmail(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email']

