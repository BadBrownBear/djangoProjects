from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from math import pi

# Create your views here.

def get_rectangle_area(request, width: int, height: int):
    sq = width*height
    return render(request, 'geometry/rectangle.html')
    # return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {sq}.')


def get_square_area(request, width: int):
    sq = width**2
    return render(request, 'geometry/square.html')
    # return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {sq}.')


def get_circle_area(request, radius: int):
    sq = round(pi, 2) * radius ** 2
    return render(request, 'geometry/circle.html')
    # return HttpResponse(f'Площадь круга радиусом {radius} равна {sq}.')


def get_rectangle_area_redirect(request, width: int, height: int):
    redirect_url = reverse('rectangle_name', args=(width, height, ))
    return HttpResponseRedirect(redirect_url)


def get_square_area_redirect(request, width: int):
    redirect_url = reverse('square_name', args=(width,))
    return HttpResponseRedirect(redirect_url)


def get_circle_area_redirect(request, radius: int):
    redirect_url = reverse('circle_name', args=(radius,))
    return HttpResponseRedirect(redirect_url)