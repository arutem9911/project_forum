from django import forms
from django.forms import ValidationError
from .models import Topic, Comment
import datetime
from accounts.models import User


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=False,
        label='Find'
    )


class TopicModelForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('title', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        widgets = {
            'comment_text': forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }
