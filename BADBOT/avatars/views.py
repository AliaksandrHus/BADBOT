from django.shortcuts import render, redirect
import random

from .models import Name144, Mouth144, Eyes144, Antenna144, \
    NameAccessoires144, EyesAccessoires144, MouthAccessoires144, RareAccessoires144

from .models import Name720, Mouth720, Eyes720, Antenna720, \
    NameAccessoires720, EyesAccessoires720, MouthAccessoires720, RareAccessoires720

from .models import Additionally


site_type = 'type-144'                          # тип сайта - 144 / 720
frame_type = 2                                  # 2 - круглая рамка / 1 - квадратная
random_list = [12, 44, 2, 19, 0, 3, 0, 0]       # стартовый набор элементов

# [модель, антенна, сенсоры, динамик, акс. модели, акс. сенсоров, акс. динамиков, редкие]


def get_elements():

    """ Функция извлечения элементов из БД """

    # Элементы 144

    name144 = Name144.objects.get(id=random_list[0])
    antenna144 = Antenna144.objects.get(id=random_list[1])
    eyes144 = Eyes144.objects.get(id=random_list[2])
    mouth144 = Mouth144.objects.get(id=random_list[3])

    if random_list[4] != 0: name_accessoires144 = NameAccessoires144.objects.get(id=random_list[4])
    else: name_accessoires144 = 0

    if random_list[5] != 0: eyes_accessoires144 = EyesAccessoires144.objects.get(id=random_list[5])
    else: eyes_accessoires144 = 0

    if random_list[6] != 0: mouth_accessoires144 = MouthAccessoires144.objects.get(id=random_list[6])
    else: mouth_accessoires144 = 0

    if random_list[7] != 0: rare_accessoires144 = RareAccessoires144.objects.get(id=random_list[7])
    else: rare_accessoires144 = 0

    # Элементы 720

    name720 = Name720.objects.get(id=random_list[0])
    antenna720 = Antenna720.objects.get(id=random_list[1])
    eyes720 = Eyes720.objects.get(id=random_list[2])
    mouth720 = Mouth720.objects.get(id=random_list[3])

    if random_list[4] != 0: name_accessoires720 = NameAccessoires720.objects.get(id=random_list[4])
    else: name_accessoires720 = 0

    if random_list[5] != 0: eyes_accessoires720 = EyesAccessoires720.objects.get(id=random_list[5])
    else: eyes_accessoires720 = 0

    if random_list[6] != 0: mouth_accessoires720 = MouthAccessoires720.objects.get(id=random_list[6])
    else: mouth_accessoires720 = 0

    if random_list[7] != 0: rare_accessoires720 = RareAccessoires720.objects.get(id=random_list[7])
    else: rare_accessoires720 = 0

    additionally = Additionally.objects.get(id=1)

    return [

        [name144, antenna144, eyes144, mouth144,
             name_accessoires144, eyes_accessoires144, mouth_accessoires144, rare_accessoires144],

        [name720, antenna720, eyes720, mouth720,
             name_accessoires720, eyes_accessoires720, mouth_accessoires720, rare_accessoires720],

        additionally
    ]


def index(request):

    """ Главная страница """

    title = 'Главная'
    global site_type

    if request.method == 'POST':

        # Кнопка изменения типа

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'change_style_144':
            site_type = 'type-144'
            return redirect('index')

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'change_style_720':
            site_type = 'type-720'
            return redirect('index')

    image_elements = get_elements()

    data = {
        'title': title,
        'site_type': site_type,

        'frame_type': frame_type,

        'name144': image_elements[0][0],
        'antenna144': image_elements[0][1],
        'eyes144': image_elements[0][2],
        'mouth144': image_elements[0][3],
        'name_accessoires144': image_elements[0][4],
        'eyes_accessoires144' : image_elements[0][5],
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
    }

    return render(request, 'index.html', data)


def create(request):

    """ Страница создания бота """

    title = 'Создать'

    global site_type
    global frame_type
    global random_list

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
            if random_list[7] == 0: random_list[7] = 10
            else: random_list[7] -= 1
            return redirect('create')

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'a-rare+':
            if random_list[7] == 10: random_list[7] = 0
            else: random_list[7] += 1
            return redirect('create')

        # Кнопка создать случайного бота

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'random':

            random_list = [random.randint(1, x) for x in [50, 50, 50, 50, 30, 30, 30, 30]]

            if random_list[4] > 10: random_list[4] = 0
            if random_list[5] > 10: random_list[5] = 0
            if random_list[6] > 10: random_list[6] = 0
            if random_list[7] > 10: random_list[7] = 0

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

    image_elements = get_elements()

    data = {

        'title': title,
        'site_type': site_type,

        'frame_type': frame_type,

        'name144': image_elements[0][0],
        'antenna144': image_elements[0][1],
        'eyes144': image_elements[0][2],
        'mouth144': image_elements[0][3],
        'name_accessoires144': image_elements[0][4],
        'eyes_accessoires144' : image_elements[0][5],
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
    }

    return render(request, 'create.html', data)


def collection(request):

    """ Страница коллекции """

    title = 'Коллекция'
    global site_type

    if request.method == 'POST':

        # Кнопка изменения типа

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'change_style_144':
            site_type = 'type-144'
            return redirect('collection')

        if 'submit_button' in request.POST and request.POST['submit_button'] == 'change_style_720':
            site_type = 'type-720'
            return redirect('collection')

    image_elements = get_elements()

    data = {

        'title': title,
        'site_type': site_type,

        'frame_type': frame_type,

        'name144': image_elements[0][0],
        'antenna144': image_elements[0][1],
        'eyes144': image_elements[0][2],
        'mouth144': image_elements[0][3],
        'name_accessoires144': image_elements[0][4],
        'eyes_accessoires144' : image_elements[0][5],
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
    }

    return render(request, 'collection.html', data)
