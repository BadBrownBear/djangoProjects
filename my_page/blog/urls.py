from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:name>', views.get_info_about_post_by_number),
    path('posts/<str:name>', views.get_info_about_post, name='post_name'),
    path('posts', views.posts),
    path('', views.index),
]