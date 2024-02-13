from  django.urls import path
from . import views 

urlpatterns = [
    path('',views.index, name='index'),
    path('counter',views.counter,name='counter'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout_user,name='logout_user'),
    path('post/<str:pk>',views.post,name='post'),
    path('operation',views.operation,name='operation'),
    path('blog',views.blog,name='blog')
]




