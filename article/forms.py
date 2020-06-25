from django import forms
from article.models import Text

class ArticleForm(forms.ModelForm):

	class Meta:
		model = Text
		fields = ['title', 'url', 'image', 'text', 'tag']

