"""
Definition of forms.
"""

import re
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))
class AnketaForm(forms.Form):
    name = forms.CharField(label = 'Ваше имя', min_length=2, max_length=50)
    secondname = forms.CharField(label = 'Ваше фамилия', min_length=2, max_length=50)
    city = forms.CharField(label = 'Город, в котором вы живете', min_length=2, max_length=50)
    shop = forms.ChoiceField(label = 'Есть ли в вашем городе наш магазин',
                             choices=[('1','Да'),('2','Нет')],
                             widget=forms.RadioSelect, initial=1)
    rate = forms.ChoiceField(label = 'Оцените пожалуйста удобство сайта, где 1 - сложно разобраться и 5 - очень удобно и просто',
                             choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    notice = forms.BooleanField(label = 'Получать интересные предложения на свой e-mail?', required=False)
    email = forms.EmailField(label = 'Ваш e-mail', min_length=7)
    comments = forms.CharField(label = 'Дополнительные комментарии', widget= forms.Textarea(attrs={'rows':12, 'cols':20}), required=False)
    
class CommentForm (forms.ModelForm):

    class Meta:

        model = Comment # используемая модель

        fields = ('text',) # требуется заполнить только поле text

        labels = {'text': "Комментарий"} # метка к полю формы text
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}