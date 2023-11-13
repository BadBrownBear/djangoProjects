from django.urls import path
from . import views

urlpatterns = [
    path('<int:day>', views.get_info_about_day_by_number),
    path('<str:day>', views.get_info_about_day, name='weeks_name'),
    path('', views.index)
]