from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models

def index(request):
	articles=models.Article.objects.all()
	return render(request,'blog/index.html',{'articles':articles})

def article_page(request,id):
	article=models.Article.objects.get(pk=id)
	return render(request,'blog/article_page.html',{'article':article})


def edit_page(request,id):
	if id==0:
		return render(request,'blog/edit_page.html')
	else:
		article=models.Article.objects.get(pk=id)
		return render(request,'blog/edit_page.html',{'article':article})



def edit_action(request):
	title=request.POST.get('title','title')
	content=request.POST.get('content','content')
	id_=request.POST.get('id')
	if int(id_)==0:
		models.Article.objects.create(title=title,content=content)
		articles=models.Article.objects.all()
		return render(request,'blog/index.html',{'articles':articles})

	else:
		article=models.Article.objects.get(pk=id_)
		article.title=title
		article.content=content
		article.save()
		return render(request,'blog/article_page.html',{'article':article})


def del_action(request,id):
	article=models.Article.objects.get(pk=id)
	article.delete()
	articles=models.Article.objects.all()
	return render(request,'blog/index.html',{'articles':articles})