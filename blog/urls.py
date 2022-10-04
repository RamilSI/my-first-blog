from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='pop_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]