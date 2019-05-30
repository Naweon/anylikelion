
from django import forms #모델폼이다
from .models import Blog

class BlogForms(forms.ModelForm):

    class Meta:
        model= Blog
        fields=('title', 'body', 'created_date',)   #fields는 form에 저장하고 싶은 것을 가져온다.