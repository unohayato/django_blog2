from django import forms

class PostForm(forms.Form):
  title = forms.CharField('タイトル', max_lengh=200) 
  content = forms.CharField('内容')
