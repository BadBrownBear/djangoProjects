from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')

urlpatterns = [
    path('', views.index),
    path('<yyyy:sign_zodiac>', views.get_yyyy_converters),
    path('<int:month>/<int:day>', views.day),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_number),
    path('<my_float:sign_zodiac>', views.get_my_float_converters),
    path('<my_date:sign_zodiac>', views.get_my_date_converters),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='horoscope_name'),
    path('type', views.types),
    path('type/<str:sign_type>', views.get_info_about_type, name='type_name'),
]