from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - <i>пятый знак зодиака</i>, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

types_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}

types_days = [
    [21, 'capricorn', 'aquarius'],
    [20, 'aquarius', 'pisces'],
    [21, 'pisces', 'aries'],
    [21, 'aries', 'taurus'],
    [22, 'taurus', 'gemini'],
    [22, 'gemini', 'cancer'],
    [23, 'cancer', 'leo'],
    [22, 'leo', 'virgo'],
    [24, 'virgo', 'libra'],
    [24, 'libra', 'scorpio'],
    [23, 'scorpio', 'sagittarius'],
    [23, 'sagittarius', 'capricorn'],
]

def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    #if description:
    return render(request, 'horoscope/info_zodiac.html', context={'description_zodiac': description, 'sign': sign_zodiac})
    #else:
    #    return HttpResponseNotFound(f'Неизвестный знак зодиака - {sign_zodiac}')


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict.keys())
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac-1]
    redirect_url = reverse('horoscope_name', args=(name_zodiac, ))
    return HttpResponseRedirect(redirect_url)


def index(request):
    zodiacs = list(zodiac_dict.keys())
    return render(request, 'horoscope/index.html', context={'zodiacs': zodiacs})
    #li_elements = ''
    #for i in zodiacs:
    #    url = reverse('horoscope_name', args=[i])
    #    li_elements += f'<li><a href="{url}">{i.title()}</a></li>'
    #return HttpResponse(f'<ul>{li_elements}</ul>')


def types(request):
    types_list = list(types_dict.keys())
    li_elements = ''
    for i in types_list:
        url = reverse('type_name', args=[i])
        li_elements += f'<li><a href="{url}">{i.title()}</a></li>'
    return HttpResponse(f'<ul>{li_elements}</ul>')


def get_info_about_type(request, sign_type: str):
    sign_list = types_dict.get(sign_type, None)
    if sign_list:
        li_elements = ''
        for i in sign_list:
            url = reverse('horoscope_name', args=[i])
            li_elements += f'<li><a href="{url}">{i.title()}</a></li>'
        return HttpResponse(f'<ul>{li_elements}</ul>')
    else:
        return HttpResponseNotFound(f'Неизвестный тип {sign_type}')


def day(request, month:int, day: int):
    if 1 <= month <= 12:
        sign_list = types_days[month-1]
        if 31 >= day >= sign_list[0]:
            sign = sign_list[2]
        elif 1 <= day < sign_list[0]:
            sign = sign_list[1]
        else:
            return HttpResponseNotFound(f'Неизвестный день {day}')
        return HttpResponse(f'<h2>{day}.{month}: {sign.title()} </h2><p>{zodiac_dict.get(sign, None)}</p>')
    else:
        return HttpResponseNotFound(f'Неизвестный месяц {month}')


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали число из 4ёх цифр — {sign_zodiac}')


def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали вещественное число — {sign_zodiac}')


def get_my_date_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали дату — {sign_zodiac}')