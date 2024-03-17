# forms.py
from django import forms
from musics.models import Comment 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("writer", "comment_text")
