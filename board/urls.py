import view
from django.urls import path
from . import views

urlpatterns = [
    # url 패턴, 설정파일명.함수명
    path('', views.index),

    path('list/', views.list),
    path('view/', views.view),
    path('write/', views.write),
    path('update/', views.update),
    path('delete/', views.delete),

]