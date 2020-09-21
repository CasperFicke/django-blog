from django import forms
from .models import Post, Category, Comment

# maak list met categorien tbv dropdown
categorien = Category.objects.all().values_list('name', 'name')
categorien_list =[]
for item in categorien:
  categorien_list.append(item)


# Form to add post
class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')

    widgets = {
      'title'    : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'insert title here'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      'author'   : forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'authorfield', 'type':'hidden'}),
      # 'author' : forms.Select(attrs={'class': 'form-control'}),
      'category' : forms.Select(choices=categorien_list, attrs={'class': 'form-control'}),
      'body'     : forms.Textarea(attrs={'class': 'form-control'}),
      'snippet'  : forms.Textarea(attrs={'class': 'form-control'}),
    }

# form to edit post
class UpdateForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'title_tag', 'body', 'snippet')

    widgets = {
      'title'    : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'insert title here'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      'body'     : forms.Textarea(attrs={'class': 'form-control'}),
      'snippet'  : forms.Textarea(attrs={'class': 'form-control'}),
    }

# Form to add comment
class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('name', 'body')

    widgets = {
      'name'    : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'insert name here'}),
      'body'     : forms.Textarea(attrs={'class': 'form-control'}),
    }
