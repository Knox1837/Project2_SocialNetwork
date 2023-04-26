from .models import ImageUpload, Post
from django import forms

class PostAddForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Post
