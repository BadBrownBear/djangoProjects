from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

week_dic = {
    'monday': 'Дела на понедельник',
    'tuesday': 'Дела на вторник',
    'wednesday': 'Дела на среду',
    'thursday': 'Дела на четверг',
    'friday': 'Дела на пятницу',
    'saturday': 'Дела на субботу',
    'sunday': 'Дела на воскресенье'
}

def get_info_about_day(request, day: str):
    description = week_dic.get(day, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Неизвестный день недели - {day}')


def get_info_about_day_by_number(request, day: int):
    weeks = list(week_dic.keys())
    if 1 <= day <= len(weeks):
        name_day = weeks[day - 1]
        redirect_url = reverse('weeks_name', args=(name_day,))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {day}')


def index(request):
    return render(request, 'week_days/greeting.html')