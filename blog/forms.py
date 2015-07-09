from django import forms

from .models import Post

class PostForm(forms.ModelForm):
	class Meta: #Diz ao Django qual modelo deve ser uado para criar o formulário (model=Post)
		model = Post
		fields = ('titulo', 'texto',) #Diz quais os campos devem entrar no formulário