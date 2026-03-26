from django import forms
from .models import ArticleImage


class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = ArticleImage
        fields = '__all__'