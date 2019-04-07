# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-03-19 14:32:54
# @Last Modified by:   Marte
# @Last Modified time: 2019-03-19 15:09:41

python -m django --version
django-admin startproject mysite
python manage.py runserver
python manage.py startapp polls
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

python manage.py runserver

python manage.py migrate
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

INSTALLED_APPS = [
    'polls.apps.PollsConfig',  #add
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
python manage.py makemigrations polls

python manage.py shell

python manage.py createsuperuser

from django.contrib import admin

from .models import Question

admin.site.register(Question)

#编写你的第一个 Django 应用，第 3 部分

from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

在 {% for %} 循环中发生的函数调用：question.choice_set.all 被解释为 Python 代码 question.choice_set.all() ，将会返回一个可迭代的 Choice 对象，这一对象可以在 {% for %} 标签内部使用。


<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
<li><a href="{% url 'app1:detail' question.id %}">{{ question.question_text }}</a></li>


from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

#使用通用视图

{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}">
body {
    background: white url("images/background.gif") no-repeat;
}

#第三部分，第四部分认真看

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question
# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
