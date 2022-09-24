from django import forms
# from django.core.exceptions import ValidationError
# from django.forms import widgets
# from .models import Article, Comment
#
#
# class UserArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ["title"]
#
#
from webapp.models import Photo, Album


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields=['img','caption','is_public']



class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["name","description","is_public"]
#
#
# class ArticleDeleteForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ["title"]
#
#     def clean_title(self):
#         title = self.cleaned_data.get("title")
#         if self.instance.title != title:
#             raise ValidationError("Названия не совпадают")
#         return title
