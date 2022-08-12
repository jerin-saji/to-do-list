from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path("<pk>", views.home,name="home"),
    path("createtask/",views.create,name='create'),
    path("deletetask/<pk>",views.delete,name='delete'),
    path("updatetask/<pk>",views.delete,name='update'),
    path("forms1/",views.formview,name='formview')
]


