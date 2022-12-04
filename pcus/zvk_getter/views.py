import json
import csv
import os
import datetime
from operator import itemgetter
import pprint

from django.shortcuts import render

from .data.fields import FIELDS, PATH, OUR
from .models import Station, Block, Generator


DATA_DIR = os.path.dirname(__file__)
SOURCE = os.path.join(PATH, 'all.csv')
TARGET = os.path.join(DATA_DIR, 'data/zvk.json')


def get_data_from_csv():
    """
    Загружаем заявки из csv файла, конвертируем всё в json
    :return: дата среза базы заявок
    """
    with open (SOURCE, encoding='utf-8') as file_data:
        data_from_file = csv.reader(file_data, delimiter=';', dialect='excel')
        data_list = list(data_from_file)

        date = data_list[0][0][-8:]
        data = data_list[2:]
        output_data = []

        for row in data:
            zvk_dict = dict(zip(FIELDS, row))
            output_data.append(zvk_dict)

    with open(TARGET, 'w', encoding='utf-8') as zvk_json:
        json.dump(output_data, zvk_json, ensure_ascii=False, indent=4)

    return str(date)


def current_shift():
    """
    Получаем строку текущей смены в завистимости от времени
    :return: str
    """
    CURRENT_DATE = datetime.datetime.now()
    NEXT_DATE = CURRENT_DATE + datetime.timedelta(days=1)
    shift = f'Дневная смена с 8:00 до 20:00 {CURRENT_DATE.strftime("%d.%m.%y")}' \
        if int(CURRENT_DATE.strftime("%H")) in range(8, 20) \
        else f'Ночная смена с 20:00 {CURRENT_DATE.strftime("%d.%m.%y")} до {NEXT_DATE.strftime("%d.%m.%y")}'

    return shift


# def get_our_all_gen():
#     zvk_dict = {}
#     all_zvk = json.load(open(TARGET, encoding='utf-8'))
#     OUR_list = []
#     for el in all_zvk:
#         if el['subject'] in OUR \
#                 and el['complex'] in ['ЭНРГ.Б', 'ЭНРГ.ТГ', 'ЭНРГ.ОО'] \
#                 and el['zvk_status'] == 'Открытая':
#             zvk_dict.update({el['self_number']: el})
#     OUR_list.append(zvk_dict)
#
#     return OUR_list

def get_our_all_gen():
    zvk_dict = {}
    all_zvk = json.load(open(TARGET, encoding='utf-8'))
    OUR_list = []


    for el in all_zvk:
        if el['subject'] in OUR \
                and el['complex'] in ['ЭНРГ.Б', 'ЭНРГ.ТГ', 'ЭНРГ.ОО'] \
                and el['zvk_status'] == 'Открытая':
            zvk_dict.update({el['self_number']: el})
    OUR_list.append(zvk_dict)

    return OUR_list




def get_all_zvk(request):
    """
    Загружаем базу заявок из json
    """
    date = get_data_from_csv()
    shift = current_shift()
    all_zvk = json.load(open(TARGET, encoding='utf-8'))

    context = {
        'zvk_test_data': 'zvk_test_data',
        'data': all_zvk,
        'date': date,
        'shift': shift,
    }

    return render(request, 'zvk_getter/zvk_getter.html', context)


def get_gen_zvk(request):
    """
    Открытые заявки по генерации
    """
    date = get_data_from_csv()
    shift = current_shift()
    all_zvk = json.load(open(TARGET, encoding='utf-8'))

    all_gen = []
    for el in all_zvk:
        if el['complex'] in ['ЭНРГ.Б', 'ЭНРГ.ТГ', 'ЭНРГ.ОО']:
            all_gen.append(el)

    context = {
        'zvk_test_data': 'zvk_test_data',
        'data': all_gen,
        'shift': shift,
        'date': date,
    }

    return render(request, 'zvk_getter/zvk_getter.html', context)


def get_all_our(request):
    data = get_our_all_gen()
    our = OUR

    stations = Station.objects.all().order_by('-rating')
    blocks = Block.objects.all().order_by('title')
    block_available_mode = Block.main_condition_choices
    generators = Generator.objects.all()

    print(block_available_mode)

    context = {
        'data': data,
        'our': our,
        'stations': stations,
        'blocks': blocks,
        'generators': generators,
    }

    return render(request, 'zvk_getter/title.html', context)


def get_single_station(request, station_id):
    station = Station.objects.get(pk=station_id)
    blank = station.title
    all_zvk = json.load(open(TARGET, encoding='utf-8'))
    all_target_zvk = []

    for el in all_zvk:
        if el['subject'] == blank:
            all_target_zvk.append(el)

    target_zvk = sorted(all_target_zvk, key=itemgetter('equipment'))

    context = {
        'station': blank,
        'zvk': target_zvk,
    }
    return render(request, 'zvk_getter/single_title.html', context)
