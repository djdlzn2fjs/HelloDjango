import view
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # url 패턴, 설정파일명.함수명
    path('', views.index),

    path('list/', views.list, name='list'),
    path('view/<int:bid>/', views.view),
    path('write/', views.write, name='write'),
    path('update/<int:bid>/', views.update),
    path('delete/<int:bid>/', views.delete),

]