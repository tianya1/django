from django.urls import path,include
from blog import views 
app_name = 'blog'

urlpatterns = [
    path('', views.index,name='index'),
    path('article/<int:id>/', views.article_page, name='article_page'),
    path('edit/<int:id>/', views.edit_page,name='edit_page'),
    path('edit/action/', views.edit_action,name='edit_action'),
    path('del/<int:id>/', views.del_action,name='del_action'),
]
