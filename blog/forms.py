from django import forms
from .models import Comment


class CommentsCreateForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
