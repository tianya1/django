# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-03-18 15:08:03
# @Last Modified by:   Marte
# @Last Modified time: 2019-03-21 21:13:05
#
django-admin startproject mysite

python manage.py runserver

python3 manage.py runserver

python manage.py startapp blog

python manage.py runserver 0:8000

python3 manage.py createsuperuser

python3 manage.py makemigrations

python3 manage.py migrate



from polls.models import Choice, Question
Question.objects.all()
from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
q.id
q.question_text
q.question_text = "What's up?"
q.save()


from django.db import models

class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text


Question.objects.filter(id=1)
Question.objects.filter(question_text__startswith='What')
Question.objects.get(pub_date__year=current_year)
 q = Question.objects.get(pk=1)
 q.choice_set.create(choice_text='Not much', votes=0)
 create add


from django.db import models
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

1. 修改app/models.py
2. 删除数据库django_content_type和django_migrations两个表中app对应的记录
3. 删除工程中app下对应的0001_initial.py

4. python manage.py makemigrations
python manage.py migrate


链接：https://www.jianshu.com/p/bc0b374efc54