from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .create_image import create_img
from .elements import get_elements

from .models import Collection
from .models import Content

import random


site_type = 'type-144'                          # тип сайта - 144 / 720
frame_type = 2                                  # 2 - круглая рамка / 1 - квадратная
random_list = [13, 44, 2, 19, 0, 3, 0, 1]       # стартовый набор элементов

image_ready = False
download_ready = False
collection_page = None

# [модель, антенна, сенсоры, динамик, акс. модели, акс. сенсоров, акс. динамиков, редкие]


def index(request):

    """ Главная страница """

    title = 'Главная'

    global site_type

    try: content = Content.objects.get(id=1)
    except: content = ''

    image_elements = get_elements(random_list)

    if request.method == 'POST':

        # Кнопка изменения типа

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'change_style_144':
            site_type = 'type-144'
            return redirect('index')

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'change_style_720':
            site_type = 'type-720'
            return redirect('index')

    data = {
        'title': title,
        'site_type': site_type,

        'frame_type': frame_type,

        'name144': image_elements[0][0],
        'antenna144': image_elements[0][1],
        'eyes144': image_elements[0][2],
        'mouth144': image_elements[0][3],
        'name_accessoires144': image_elements[0][4],
        'eyes_accessoires144': image_elements[0][5],
        'mouth_accessoires144': image_elements[0][6],
        'rare_accessoires144': image_elements[0][7],

        'name720': image_elements[1][0],
        'antenna720': image_elements[1][1],
        'eyes720': image_elements[1][2],
        'mouth720': image_elements[1][3],
        'name_accessoires720': image_elements[1][4],
        'eyes_accessoires720': image_elements[1][5],
        'mouth_accessoires720': image_elements[1][6],
        'rare_accessoires720': image_elements[1][7],

        'additionally': image_elements[2],

        'content': content,
    }

    return render(request, 'index.html', data)


def create(request):

    """ Страница создания бота """

    title = 'Создать'

    global site_type
    global frame_type
    global random_list
    global image_ready
    global download_ready

    try: content = Content.objects.get(id=1)
    except: content = ''

    if not download_ready: image_ready = False
    if image_ready and download_ready: download_ready = False

    image_elements = get_elements(random_list)
    all_elements_id = Collection.objects.values_list('elements_id', flat=True)

    if '-'.join([str(x) for x in random_list]) in all_elements_id:
        image_in_db = Collection.objects.get(elements_id='-'.join([str(x) for x in random_list]))
    else: image_in_db = False

    if request.method == 'POST':

        # Кнопка изменения 144 / 720

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'change_style_144':
            site_type = 'type-144'
            return redirect('create')

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'change_style_720':
            site_type = 'type-720'
            return redirect('create')

        # Кнопка изменить модель

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'model-':
            if random_list[0] == 1: random_list[0] = 50
            else: random_list[0] -= 1
            return redirect('create')

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'model+':
            if random_list[0] == 50: random_list[0] = 1
            else: random_list[0] += 1
            return redirect('create')

        # Кнопка изменить антенну

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'antenna-':
            if random_list[1] == 1: random_list[1] = 50
            else: random_list[1] -= 1
            return redirect('create')

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'antenna+':
            if random_list[1] == 50: random_list[1] = 1
            else: random_list[1] += 1
            return redirect('create')

        # Кнопка изменить сенсор

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'sensor-':
            if random_list[2] == 1: random_list[2] = 50
            else: random_list[2] -= 1

            if random_list[5] != 1: random_list[5] = 0
            return redirect('create')

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'sensor+':
            if random_list[2] == 50: random_list[2] = 1
            else: random_list[2] += 1

            if random_list[5] != 1: random_list[5] = 0
            return redirect('create')

        # Кнопка изменить динамик

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'speaker-':
            if random_list[3] == 1: random_list[3] = 50
            else: random_list[3] -= 1
            return redirect('create')

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'speaker+':
            if random_list[3] == 50: random_list[3] = 1
            else: random_list[3] += 1
            return redirect('create')

        # Кнопка изменить аксессуары модели

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'a-model-':
            if random_list[4] == 0: random_list[4] = 10
            else: random_list[4] -= 1
            return redirect('create')

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'a-model+':
            if random_list[4] == 10: random_list[4] = 0
            else: random_list[4] += 1
            return redirect('create')

        # Кнопка изменить аксессуары глаз

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'a-sensor-':
            if random_list[5] == 0: random_list[5] = 10
            else: random_list[5] -= 1
            return redirect('create')

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'a-sensor+':
            if random_list[5] == 10: random_list[5] = 0
            else: random_list[5] += 1
            return redirect('create')

        # Кнопка изменить аксессуары рта

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'a-speaker-':
            if random_list[6] == 0: random_list[6] = 10
            else: random_list[6] -= 1
            return redirect('create')

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'a-speaker+':
            if random_list[6] == 10: random_list[6] = 0
            else: random_list[6] += 1
            return redirect('create')

        # Кнопка изменить редкие аксессуары

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'a-rare-':
            if random_list[7] == 0: random_list[7] = 50
            else: random_list[7] -= 1
            return redirect('create')

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'a-rare+':
            if random_list[7] == 50: random_list[7] = 0
            else: random_list[7] += 1
            return redirect('create')

        # Кнопка создать случайного бота

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'random':

            random_list = [random.randint(1, x) for x in [50, 50, 50, 50, 40, 40, 40, 50]]

            if random_list[4] > 10: random_list[4] = 0
            if random_list[5] > 10: random_list[5] = 0
            if random_list[6] > 10: random_list[6] = 0
            # if random_list[7] > 10: random_list[7] = 0

            return redirect('create')

        # Кнопка изменить рамку

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'frame':
            frame_type = 2 if frame_type == 1 else 1
            return redirect('create')

        # Кнопка удалить аксессуары модели

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'a-model-delete':
            random_list[4] = 0
            return redirect('create')

        # Кнопка удалить аксессуары глаз

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'a-sensor-delete':
            random_list[5] = 0
            return redirect('create')

        # Кнопка удалить аксессуары рта

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'a-speaker-delete':
            random_list[6] = 0
            return redirect('create')

        # Кнопка удалить редкие аксессуары

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'a-rare-delete':
            random_list[7] = 0
            return redirect('create')

        # Кнопка скачать картинку

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'download-image':

            if image_in_db: image_ready = image_in_db
            else: image_ready = create_img(image_elements, random_list)

            download_ready = True
            return redirect('create')

    data = {

        'title': title,
        'site_type': site_type,

        'frame_type': frame_type,

        'name144': image_elements[0][0],
        'antenna144': image_elements[0][1],
        'eyes144': image_elements[0][2],
        'mouth144': image_elements[0][3],
        'name_accessoires144': image_elements[0][4],
        'eyes_accessoires144': image_elements[0][5],
        'mouth_accessoires144': image_elements[0][6],
        'rare_accessoires144': image_elements[0][7],

        'name720': image_elements[1][0],
        'antenna720': image_elements[1][1],
        'eyes720': image_elements[1][2],
        'mouth720': image_elements[1][3],
        'name_accessoires720': image_elements[1][4],
        'eyes_accessoires720': image_elements[1][5],
        'mouth_accessoires720': image_elements[1][6],
        'rare_accessoires720': image_elements[1][7],

        'additionally': image_elements[2],
        'image_in_db': image_in_db,
        'image_ready': image_ready,

        'content': content,
    }

    return render(request, 'create.html', data)


def collection(request):

    """ Страница коллекции """

    title = 'Коллекция'
    global site_type
    global random_list
    global collection_page

    try: content = Content.objects.get(id=1)
    except: content = ''

    image_elements = get_elements(random_list)

    max_id_object = Collection.objects.all().order_by('-image_id').first().image_id

    data = Collection.objects.all().order_by('image_id')
    paginator = Paginator(data, 100)
    page_get = request.GET.get('page')

    if page_get != None: collection_page = page_get

    page_number = collection_page
    collection_elements = paginator.get_page(page_number)

    if request.method == 'POST':

        # Кнопка изменения типа

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'change_style_144':
            site_type = 'type-144'
            return redirect('collection')

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'change_style_720':
            site_type = 'type-720'
            return redirect('collection')

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'edit':
            random_list = list(map(int, request.POST['elements'].split('-')))
            return redirect('create')

    data = {

        'title': title,
        'site_type': site_type,

        'frame_type': frame_type,

        'name144': image_elements[0][0],
        'antenna144': image_elements[0][1],
        'eyes144': image_elements[0][2],
        'mouth144': image_elements[0][3],
        'name_accessoires144': image_elements[0][4],
        'eyes_accessoires144': image_elements[0][5],
        'mouth_accessoires144': image_elements[0][6],
        'rare_accessoires144': image_elements[0][7],

        'name720': image_elements[1][0],
        'antenna720': image_elements[1][1],
        'eyes720': image_elements[1][2],
        'mouth720': image_elements[1][3],
        'name_accessoires720': image_elements[1][4],
        'eyes_accessoires720': image_elements[1][5],
        'mouth_accessoires720': image_elements[1][6],
        'rare_accessoires720': image_elements[1][7],

        'additionally': image_elements[2],

        'collection_elements': collection_elements,
        'page_number': str(page_number) if page_number else '0',
        'bots_on_page': f'#{collection_elements[0].image_id} - #{collection_elements[-1].image_id}',
        'max_id_object': max_id_object,

        'content': content,
    }

    return render(request, 'collection.html', data)
