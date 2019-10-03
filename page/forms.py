from django.forms import ModelForm
from .models import Post

class Postform(ModelForm):
    class Meta:
        model=Post
        fields=('title','content',)
    # title=forms.CharField(max_length=300)
    # text=forms.CharField()
