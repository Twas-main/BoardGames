"""
Definition of views.
"""

from datetime import datetime
import re
from django.shortcuts import render
from django.http import HttpRequest
from .forms import AnketaForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.db import models
from .models import Blog
from .models import Comment # использование модели комментариев
from .forms import CommentForm # использование формы ввода комментария
from .forms import BlogForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'year':datetime.now().year,
        }
    )
def res(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/res.html',
        {
            'title':'Полезные ресурсы',
            'year':datetime.now().year,
        }
    )
def pool(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    data = None
    shop = {'1': 'Да', '2': 'Нет'}
    rate = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5'}
    if request.method == 'POST':
        form = AnketaForm(request.POST)
        if form.is_valid():
            data = dict();
            data['name'] = form.cleaned_data['name']
            data['secondname'] = form.cleaned_data['secondname']
            data['city'] = form.cleaned_data['city']
            data['shop'] =shop[ form.cleaned_data['shop']]
            data['rate'] =rate[ form.cleaned_data['rate']]
            if (form.cleaned_data ['notice']==True):
                data['notice'] = 'Да'
            else:
                data['notice'] = 'Нет'
            data['email'] = form.cleaned_data['email']
            data['comments'] = form.cleaned_data['comments']
            form = None
    else:
        form = AnketaForm()
    return render(
        request,
        'app/pool.html',
        {
            'form':form,
            'data': data
        }
    )

def registration(request):

    """Renders the registration page."""

    assert isinstance(request, HttpRequest)

    if request.method == "POST": # после отправки формы

        regform = UserCreationForm (request.POST)

        if regform.is_valid(): #валидация полей формы

            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы

            reg_f.is_staff = False # запрещен вход в административный раздел

            reg_f.is_active = True # активный пользователь

            reg_f.is_superuser = False # не является суперпользователем

            reg_f.date_joined = datetime.now() # дата регистрации

            reg_f.last_login = datetime.now() # дата последней авторизации

            reg_f.save() # сохраняем изменения после добавления данных

        return redirect('home') # переадресация на главную страницу после регистрации

    else:

        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя

    return render(

    request,

    'app/registration.html',

    {

    'regform': regform, # передача формы в шаблон веб-страницы

    'year':datetime.now().year,

    }

)

def blog(request):

    """Renders the blog page."""

    assert isinstance(request, HttpRequest)

    posts = Blog.objects.all() # запрос на выбор всех статей блога из модели

    return render(

        request,

        'app/blog.html',

        {

        'title':'Блог',

        'posts': posts, # передача списка статей в шаблон веб-страницы

        'year':datetime.now().year,

        }

)

def blogpost(request, parametr):

    """Renders the blogpost page."""

    assert isinstance(request, HttpRequest)

    post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(post=parametr)
    if request.method == "POST": # после отправки данных формы на сервер методом POST

        form = CommentForm(request.POST)

        if form.is_valid():

            comment_f = form.save(commit=False)

            comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя

            comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату

            comment_f.post = Blog.objects.get(id=parametr) # добавляем в модель Комментария (Comment) статью, для которой данный комментарий

            comment_f.save() # сохраняем изменения после добавления полей

        return redirect('blogpost', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки комментария

    else:
        form = CommentForm() # создание формы для ввода комментария
    return render(

        request,
       
        'app/blogpost.html',

            {

                'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы

                'year':datetime.now().year,
                'comments': comments, # передача всех комментариев к данной статье в шаблон веб-страницы
                'form': form, # передача формы добавления комментария в шаблон веб-страницы
            }

)

def newpost(request):
    
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.autor = request.user
            blog_f.save()
            return redirect('blog')
        
    else:
              blogform = BlogForm()
    return render(
            request,
            'app/newpost.html',
            {
                'title': 'Добавить статью блога',
                'blogform': blogform,
                'year': datetime.now().year,
            }
        )
def videoposts(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    
    return render(
        request,
        'app/videoposts.html',
        {
            'title':'Видео',
            'year':datetime.now().year,
        }
    )