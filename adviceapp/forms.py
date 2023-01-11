from .models import Article_comments
from django import forms

class Article_commentsForm(forms.ModelForm):
    class Meta:
        model = Article_comments
        fields = ('body',)