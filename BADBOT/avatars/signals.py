from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .elements import get_elements
from .create_image import create_img

import os


@receiver(post_migrate)
def create_data(apps, sender, **kwargs):

    """ Создание записей в БД при миграции """

    if sender.name == 'avatars':

        for mod in ['Name', 'Mouth', 'Eyes', 'Antenna',
                    'MouthAccessoires', 'EyesAccessoires', 'NameAccessoires', 'RareAccessoires']:

            Model = apps.get_model('avatars', f'{mod}144')

            for image_file in os.listdir(f'media/image/144/{mod}/'):

                if image_file[0] == '+':

                    create = Model()
                    create.id = int(image_file.split('_')[1])
                    create.name_ru = image_file.split('_')[-1].split('.')[0].replace('+', ' ')
                    create.name_en = image_file.split('_')[-2].replace('+', ' ')
                    create.element1 = f'media/image/144/{mod}/{image_file}'

                    if image_file[1] == '-':
                        create.element2 = f'media/image/144/{mod}/-+{image_file[2:]}'

                    create.save()

        for mod in ['Name', 'Mouth', 'Eyes', 'Antenna',
                    'MouthAccessoires', 'EyesAccessoires', 'NameAccessoires', 'RareAccessoires']:

            Model = apps.get_model('avatars', f'{mod}720')

            for image_file in os.listdir(f'media/image/720/{mod}/'):

                if image_file[0] == '+':

                    create = Model()
                    create.id = int(image_file.split('_')[1])
                    create.name_ru = image_file.split('_')[-1].split('.')[0].replace('+', ' ')
                    create.name_en = image_file.split('_')[-2].replace('+', ' ')
                    create.element1 = f'media/image/720/{mod}/{image_file}'

                    if image_file[1] == '-':
                        create.element2 = f'media/image/720/{mod}/-+{image_file[len(image_file.split("_")[0]):]}'

                    if image_file[2] == '-':
                        create.element3 = f'media/image/720/{mod}/--+{image_file[3:]}'

                    create.save()

        # Создание фона м рамки в БД

        Model = apps.get_model('avatars', 'Additionally')

        create = Model()
        create.id = 1
        create.background = 'media/image/additionally/BG.png'
        create.frame = 'media/image/additionally/frame.png'
        create.save()

        # Создание стартовой коллекции

        random_list_set = [[3, 15, 2, 43, 0, 0, 0, 28], [13, 23, 19, 9, 0, 0, 0, 26], [24, 21, 48, 49, 0, 0, 0, 11],
                           [18, 34, 5, 20, 0, 0, 0, 34], [29, 6, 12, 33, 3, 0, 2, 45], [8, 10, 10, 25, 0, 0, 3, 35],
                           [39, 18, 17, 3, 0, 0, 0, 6], [18, 21, 24, 13, 0, 0, 0, 34], [48, 24, 3, 19, 0, 0, 0, 36],
                           [3, 6, 31, 22, 0, 0, 0, 18], [13, 30, 30, 41, 7, 0, 1, 13], [19, 27, 38, 49, 0, 0, 0, 36],
                           [44, 24, 40, 12, 0, 6, 0, 20], [10, 10, 35, 45, 8, 0, 10, 46], [2, 3, 2, 1, 0, 0, 0, 8],]
                           # [19, 36, 48, 25, 0, 0, 0, 32], [16, 27, 11, 48, 8, 0, 0, 3], [13, 39, 9, 9, 1, 0, 0, 38],
                           # [24, 7, 1, 37, 0, 1, 0, 11], [4, 30, 48, 45, 0, 0, 5, 3], [44, 10, 39, 33, 0, 0, 0, 48],
                           # [39, 30, 34, 13, 0, 0, 0, 28], [9, 28, 12, 22, 0, 0, 0, 11], [28, 23, 37, 19, 0, 0, 0, 22],
                           # [13, 7, 19, 15, 0, 0, 0, 7], [16, 2, 41, 36, 0, 0, 6, 33], [24, 7, 18, 45, 0, 0, 0, 34],
                           # [12, 12, 22, 20, 0, 3, 3, 7], [47, 5, 26, 33, 0, 0, 0, 3], [38, 36, 14, 43, 10, 0, 0, 47],
                           # [29, 40, 37, 30, 8, 0, 3, 9], [16, 7, 50, 25, 0, 0, 0, 33], [21, 36, 29, 24, 0, 8, 0, 13],
                           # [23, 30, 33, 2, 0, 0, 0, 15], [39, 44, 42, 1, 0, 0, 0, 31], [31, 19, 3, 35, 0, 0, 3, 40],
                           # [11, 7, 48, 1, 5, 0, 0, 32], [14, 28, 30, 6, 0, 0, 0, 44], [4, 44, 12, 19, 0, 0, 5, 36],
                           # [33, 7, 44, 13, 0, 0, 0, 4], [14, 15, 43, 32, 0, 0, 0, 17], [38, 31, 12, 27, 0, 0, 6, 37],
                           # [18, 30, 38, 5, 0, 0, 0, 40], [38, 15, 28, 41, 0, 0, 9, 11], [3, 19, 39, 31, 0, 0, 3, 40],
                           # [28, 6, 1, 23, 0, 0, 0, 36], [38, 31, 26, 20, 0, 0, 0, 5], [44, 15, 4, 13, 0, 0, 0, 14],
                           # [44, 27, 37, 43, 10, 0, 0, 21], [14, 30, 45, 27, 0, 0, 0, 15], [27, 41, 48, 22, 0, 0, 0, 6],
                           # [44, 42, 32, 26, 0, 0, 6, 29], [19, 48, 12, 50, 0, 0, 0, 28], [1, 18, 19, 8, 0, 0, 9, 31],
                           # [11, 47, 15, 9, 0, 0, 3, 22], [14, 13, 41, 16, 0, 0, 0, 18], [49, 6, 35, 48, 0, 0, 0, 3],
                           # [49, 10, 37, 11, 2, 0, 0, 33], [9, 12, 10, 33, 0, 0, 0, 40], [2, 21, 22, 43, 0, 0, 0, 32],
                           # [15, 30, 4, 30, 0, 0, 0, 50], [39, 15, 13, 19, 0, 7, 0, 9], [3, 42, 5, 46, 0, 0, 0, 17],
                           # [25, 38, 12, 35, 0, 4, 4, 26], [28, 32, 47, 31, 8, 0, 0, 47], [44, 28, 31, 2, 0, 0, 0, 50],
                           # [15, 27, 13, 15, 3, 0, 0, 8], [32, 15, 48, 49, 0, 0, 0, 42], [40, 30, 45, 47, 0, 0, 0, 22],
                           # [39, 10, 38, 30, 0, 0, 0, 19], [9, 14, 12, 33, 0, 0, 0, 11], [19, 41, 48, 39, 10, 0, 1, 22],
                           # [23, 4, 2, 13, 0, 0, 0, 31], [39, 9, 19, 1, 0, 0, 8, 28], [34, 32, 4, 24, 0, 0, 0, 37],
                           # [18, 23, 37, 41, 0, 0, 0, 21], [11, 3, 47, 12, 0, 0, 0, 18], [18, 9, 10, 26, 0, 0, 0, 28],
                           # [3, 18, 41, 6, 0, 0, 0, 38], [24, 2, 28, 43, 0, 0, 0, 7], [13, 6, 38, 15, 0, 0, 10, 42],
                           # [3, 1, 7, 40, 0, 0, 0, 22], [19, 49, 26, 34, 0, 0, 0, 44], [1, 23, 30, 31, 0, 0, 0, 9],
                           # [44, 44, 37, 20, 2, 0, 0, 32], [8, 7, 7, 25, 2, 0, 0, 26], [19, 13, 35, 24, 0, 6, 0, 35],
                           # [13, 10, 19, 14, 0, 0, 0, 29], [13, 27, 3, 10, 0, 0, 0, 6], [20, 38, 18, 21, 0, 0, 0, 46],
                           # [38, 2, 24, 43, 0, 0, 0, 47], [18, 12, 33, 29, 0, 0, 0, 1], [23, 18, 15, 2, 0, 0, 0, 18],
                           # [12, 48, 13, 8, 0, 0, 0, 37], [20, 18, 10, 49, 8, 0, 0, 39], [28, 9, 22, 12, 0, 0, 0, 48],
                           # [43, 21, 7, 24, 0, 0, 3, 32], [35, 19, 38, 44, 0, 0, 3, 33], [44, 23, 2, 25, 0, 0, 10, 15],
                           # [6, 49, 48, 13, 0, 0, 6, 43], [39, 36, 29, 41, 0, 0, 1, 35], [11, 41, 15, 19, 0, 0, 0, 24],
                           # [43, 17, 48, 12, 0, 0, 0, 44], [39, 13, 1, 37, 0, 0, 0, 12], [44, 32, 5, 31, 2, 0, 0, 5],
                           # [19, 44, 45, 25, 0, 0, 10, 17], [50, 23, 31, 47, 0, 0, 0, 7], [23, 36, 3, 22, 0, 0, 0, 45],
                           # [20, 19, 44, 35, 0, 0, 0, 14], [13, 23, 32, 36, 0, 0, 0, 41], [11, 26, 14, 3, 5, 0, 0, 8],
                           # [34, 18, 17, 13, 0, 0, 0, 37], [29, 42, 33, 30, 0, 0, 0, 18], [16, 30, 35, 49, 0, 0, 10, 50],
                           # [38, 21, 43, 8, 0, 0, 0, 49], [23, 15, 23, 12, 0, 0, 0, 7], [50, 38, 12, 34, 0, 0, 0, 16],
                           # [26, 50, 19, 45, 0, 0, 0, 13], [46, 15, 37, 41, 0, 0, 0, 25], [2, 6, 48, 33, 8, 0, 0, 30],
                           # [13, 31, 26, 49, 0, 0, 0, 34], [8, 13, 24, 24, 0, 0, 0, 39], [3, 40, 13, 45, 0, 0, 0, 43],
                           # [38, 7, 46, 43, 0, 0, 0, 21], [45, 8, 15, 15, 0, 0, 0, 7], [21, 10, 29, 39, 0, 0, 0, 11],
                           # [8, 26, 1, 8, 0, 0, 0, 47], [47, 32, 45, 21, 0, 0, 0, 42], [38, 13, 10, 30, 0, 0, 0, 6],
                           # [18, 30, 23, 3, 0, 0, 0, 38], [39, 30, 50, 12, 0, 0, 0, 37], [44, 32, 40, 36, 0, 0, 0, 28],
                           # [36, 14, 41, 31, 0, 0, 0, 32], [13, 44, 2, 19, 0, 3, 0, 1], [21, 27, 7, 1, 0, 0, 0, 38],
                           # [15, 46, 46, 24, 0, 0, 6, 40], [40, 29, 3, 22, 0, 0, 0, 12], [48, 23, 14, 25, 0, 0, 4, 9],
                           # [20, 1, 19, 13, 0, 0, 0, 45], [20, 45, 1, 20, 0, 7, 0, 50], [39, 14, 1, 33, 0, 0, 8, 9],
                           # [7, 38, 45, 10, 0, 0, 0, 36], [29, 50, 23, 27, 0, 0, 0, 13], [43, 46, 22, 21, 0, 0, 0, 21],
                           # [28, 2, 12, 36, 0, 0, 0, 29], [24, 34, 34, 48, 0, 2, 2, 37], [38, 34, 6, 43, 7, 0, 1, 9],
                           # [20, 6, 4, 20, 0, 0, 5, 13], [12, 40, 48, 12, 0, 0, 0, 33], [12, 16, 11, 9, 0, 0, 0, 45],
                           # [43, 2, 28, 30, 0, 0, 0, 29], [15, 25, 43, 34, 0, 0, 0, 24], [15, 18, 44, 36, 0, 0, 0, 45],
                           # [29, 4, 1, 48, 0, 0, 0, 46], [13, 29, 10, 35, 0, 0, 2, 30], [27, 15, 12, 11, 0, 0, 0, 45],
                           # [9, 33, 43, 49, 2, 6, 7, 33], [23, 21, 47, 16, 0, 0, 0, 23], [25, 12, 11, 31, 0, 0, 0, 43],
                           # [28, 12, 38, 6, 0, 0, 0, 39], [23, 42, 45, 40, 0, 0, 0, 25], [21, 10, 14, 1, 0, 0, 0, 7],
                           # [31, 41, 39, 43, 8, 0, 0, 14], [18, 40, 23, 20, 0, 0, 0, 35], [17, 39, 37, 15, 0, 0, 0, 5],
                           # [48, 45, 46, 4, 0, 0, 6, 4], [42, 9, 3, 21, 0, 0, 0, 41], [20, 21, 49, 25, 0, 0, 0, 49],
                           # [23, 38, 47, 24, 0, 0, 0, 40], [26, 41, 31, 49, 0, 0, 0, 18], [4, 36, 12, 32, 2, 0, 0, 43],
                           # [26, 30, 19, 36, 0, 0, 0, 39], [49, 43, 37, 10, 0, 8, 0, 49], [17, 26, 26, 6, 0, 0, 0, 13],
                           # [30, 40, 32, 3, 0, 0, 0, 22], [1, 6, 9, 43, 0, 0, 0, 23], [48, 15, 41, 45, 0, 0, 0, 44],
                           # [6, 14, 16, 27, 0, 0, 2, 31], [30, 26, 7, 41, 0, 4, 0, 8], [39, 33, 14, 33, 0, 0, 0, 12],
                           # [11, 50, 39, 24, 0, 0, 0, 26], [19, 44, 3, 41, 1, 0, 2, 20], [5, 47, 29, 12, 0, 0, 0, 10],
                           # [43, 5, 12, 14, 0, 0, 0, 3], [42, 20, 48, 37, 0, 0, 1, 2], [21, 36, 13, 39, 0, 0, 0, 10],
                           # [13, 6, 5, 16, 0, 0, 0, 36], [28, 38, 23, 49, 8, 0, 0, 1], [43, 23, 31, 43, 0, 0, 6, 50],
                           # [28, 16, 19, 44, 0, 0, 0, 40], [30, 34, 46, 36, 0, 0, 1, 43], [38, 4, 30, 34, 0, 0, 0, 21],
                           # [17, 49, 2, 35, 9, 0, 0, 44], [38, 7, 11, 9, 0, 4, 0, 34], [7, 17, 11, 15, 0, 0, 0, 5],
                           # [34, 44, 44, 24, 0, 0, 0, 25], [14, 23, 1, 16, 0, 0, 6, 32], [5, 37, 31, 25, 0, 0, 0, 46],
                           # [48, 29, 6, 6, 2, 3, 0, 41], [43, 7, 3, 8, 0, 0, 5, 35], [5, 41, 47, 49, 0, 0, 0, 10],
                           # [11, 42, 12, 6, 0, 0, 5, 47], [14, 38, 48, 41, 4, 0, 0, 37], [48, 44, 41, 3, 0, 0, 9, 22],
                           # [10, 28, 28, 13, 0, 0, 0, 39], [28, 17, 11, 33, 0, 0, 3, 11], [25, 40, 24, 25, 0, 0, 0, 38],
                           # [10, 21, 30, 10, 0, 0, 10, 47], [8, 22, 37, 49, 0, 0, 0, 34], [14, 44, 15, 15, 0, 0, 0, 46],
                           # [38, 50, 18, 48, 0, 0, 0, 43], [18, 15, 2, 2, 0, 0, 0, 26], [28, 14, 39, 30, 0, 0, 2, 15],
                           # [15, 48, 1, 20, 10, 0, 0, 1], [34, 30, 48, 19, 0, 0, 0, 29], [13, 20, 38, 37, 0, 0, 10, 36],
                           # [38, 10, 7, 49, 0, 0, 0, 5], [44, 18, 47, 36, 0, 0, 0, 22], [42, 40, 9, 25, 0, 0, 0, 49],
                           # [3, 10, 18, 19, 0, 0, 1, 45], [38, 28, 46, 49, 0, 0, 10, 1], [18, 40, 5, 5, 0, 1, 0, 29],
                           # [16, 13, 12, 14, 0, 0, 0, 10], [23, 39, 20, 43, 0, 0, 0, 25], [40, 18, 33, 33, 0, 0, 0, 36],
                           # [3, 13, 12, 33, 0, 0, 0, 29], [17, 30, 24, 25, 0, 0, 0, 1], [30, 15, 48, 21, 0, 0, 0, 32],
                           # [45, 23, 2, 43, 0, 0, 1, 50], [13, 12, 19, 22, 2, 0, 0, 33], [9, 34, 46, 36, 0, 0, 0, 23],
                           # [12, 10, 13, 49, 7, 0, 0, 48], [3, 18, 3, 6, 0, 0, 0, 30], [24, 23, 22, 48, 10, 6, 0, 17],
                           # [15, 41, 38, 9, 0, 0, 0, 48], [33, 39, 12, 27, 0, 0, 6, 10], [4, 44, 37, 43, 0, 0, 0, 29],
                           # [20, 3, 31, 12, 0, 0, 0, 23], [43, 26, 11, 32, 0, 0, 0, 39], [42, 14, 35, 20, 0, 0, 0, 41]]

        tot_bots = len(random_list_set)

        for num, random_list in enumerate(random_list_set, start=1):

            image_elements = get_elements(random_list)
            create_img(image_elements, random_list)

            percent_complete = round((num / tot_bots) * 100)

            print(f'\rCreate bots in collection: '
                  f'[{"■" * (percent_complete // 10)}{" " * (10 - percent_complete // 10)}] {percent_complete}% ',
                  end=' ' if num != tot_bots else '\n')

        # Создание контента в БД

        Model = apps.get_model('avatars', 'Content')

        create = Model()
        create.id = 1

        # Главная

        create.index_text_1_ru = '<h1>Пример текста h1</h1>\n'
        create.index_text_1_ru += '<h2>Пример текста h2</h2>\n'
        create.index_text_1_ru += '<h3>Пример текста h3</h3>\n'
        create.index_text_1_ru += '<h4>Пример текста h4</h4>\n'

        create.index_text_1_ru += '<p>Пример текста p</p>\n'
        create.index_text_1_ru += '<p>Пример <i>*наклонного</i> текста p</p>\n'
        create.index_text_1_ru += '<p>Пример <b>жирного</b> текста p</p>\n'

        create.index_text_1_ru += '<p>Это: <a href="http://127.0.0.1:8000/">внутренняя ссылка</a></p>\n'
        create.index_text_1_ru += '<p>Это: <a href="http://127.0.0.1:8000/" target="_blank">внешняя ссылка</a></p>\n'

        create.index_text_1_ru += '<img src="/media/design/content/index-1.jpg">\n'                 # обычная картинка
        create.index_text_1_ru += '<img id="big-image" src="/media/design/content/index-1.jpg">\n'  # большая картинка

        create.index_text_2_ru = '<h1>Пример второго блока текста</h1>\n'
        create.index_text_2_ru += '<p>Пример текста второго блока</p>\n'

        # en

        create.index_text_1_en = '<h1>Sample text h1</h1>\n'
        create.index_text_1_en += '<h2>Sample text h2</h2>\n'
        create.index_text_1_en += '<h3>Sample text h3</h3>\n'
        create.index_text_1_en += '<h4>Sample text h4</h4>\n'

        create.index_text_1_en += '<p>Sample text p</p>\n'
        create.index_text_1_en += '<p>Sample <i>*oblique</i> text p</p>\n'
        create.index_text_1_en += '<p>Sample <b>bold</b> text p</p>\n'

        create.index_text_1_en += '<p>This: <a href="http://127.0.0.1:8000/">internal link</a></p>\n'
        create.index_text_1_en += '<p>This: <a href="http://127.0.0.1:8000/" target="_blank">external link</a></p>\n'

        create.index_text_1_en += '<img src="/media/design/content/index-1.jpg">\n'                 # обычная картинка
        create.index_text_1_en += '<img id="big-image" src="/media/design/content/index-1.jpg">\n'  # большая картинка

        create.index_text_2_en = '<h1>Example of the second block of text</h1>\n'
        create.index_text_2_en += '<p>Example of the text of the second block</p>\n'

        # Конструктор

        create.create_text_1_ru = '<h3>Пример текста конструктора #1</h3>\n'
        create.create_text_1_ru += '<p>Пример текста конструктора #1</p>\n'

        create.create_text_1_ru += '<img src="/media/design/content/index-1.jpg">\n'

        create.create_text_2_ru = '<h3>Пример текста конструктора #2</h3>\n'
        create.create_text_2_ru += '<p>Пример текста конструктора #2</p>\n'

        # en

        create.create_text_1_en = '<h3>Example of the constructor text #1</h3>\n'
        create.create_text_1_en += '<p>Example of the constructor text #1</p>\n'

        create.create_text_1_en += '<img src="/media/design/content/index-1.jpg">\n'

        create.create_text_2_en = '<h3>Example of the constructor text #2</h3>\n'
        create.create_text_2_en += '<p>Example of the constructor text #2</p>\n'

        # Коллекция

        create.collection_text_1_ru = '<h3>Пример текста коллекции #1</h3>\n'
        create.collection_text_1_ru += '<p>Пример текста коллекции #1</p>\n'

        create.collection_text_1_ru += '<img src="/media/design/content/index-1.jpg">\n'

        create.collection_text_2_ru = '<h3>Пример текста коллекции #2</h3>\n'
        create.collection_text_2_ru += '<p>Пример текста коллекции #2</p>\n'

        # en

        create.collection_text_1_en = '<h3>Example of the collection text #1</h3>\n'
        create.collection_text_1_en += '<p>Example of the collection text #1</p>\n'

        create.collection_text_1_en += '<img src="/media/design/content/index-1.jpg">\n'

        create.collection_text_2_en = '<h3>Example of the collection text #2</h3>\n'
        create.collection_text_2_en += '<p>Example of the collection text #2</p>\n'

        # Картинка

        create.index_img_1 = 'media/design/content/index-1.jpg'

        # Оповещения

        create.index_message_ru = '<h4>Пример оповещения на главной странице<h4>'
        create.create_message_ru = '<h4>Пример оповещения на странице конструктора<h4>'
        create.collection_message_ru = '<h4>Пример оповещения на странице коллекции<h4>'

        create.index_message_en = '<h4>An example of an alert on the main page<h4>'
        create.create_message_en = '<h4>An example of an alert on the constructor page<h4>'
        create.collection_message_en = '<h4>Example of an alert on the collection page<h4>'

        create.save()

        # Создание футера в БД

        Model = apps.get_model('avatars', 'Footer')

        create = Model()
        create.id = 1

        # блок ссылок ru

        create.footer_box_1_name_ru = 'Ссылки'
        create.footer_link_1_1_ru = '<a href="http://127.0.0.1:8000/create/" target="_blank">Коллекция NFT Badbot 144p</a>'
        create.footer_link_1_2_ru = '<a href="http://127.0.0.1:8000/create/" target="_blank">Коллекция NFT Badbot 720p</a>'
        create.footer_link_1_3_ru = '<a href="http://127.0.0.1:8000/create/" target="_blank">Сообщество Twitter</a>'
        create.footer_link_1_4_ru = '<a href="http://127.0.0.1:8000/create/" target="_blank">Сообщество Instagram</a>'

        create.footer_box_2_name_ru = 'Информация'
        create.footer_link_2_1_ru = '<a href="http://127.0.0.1:8000/create/" target="_blank">Об авторе</a>'
        create.footer_link_2_2_ru = '<a href="http://127.0.0.1:8000/create/" target="_blank">Instagram</a>'

        # en

        create.footer_box_1_name_en = 'Links'
        create.footer_link_1_1_en = '<a href="http://127.0.0.1:8000/create/" target="_blank">Collection NFT Badbot 144p</a>'
        create.footer_link_1_2_en = '<a href="http://127.0.0.1:8000/create/" target="_blank">Collection NFT Badbot 720p</a>'
        create.footer_link_1_3_en = '<a href="http://127.0.0.1:8000/create/" target="_blank">Community Twitter</a>'
        create.footer_link_1_4_en = '<a href="http://127.0.0.1:8000/create/" target="_blank">Community Instagram</a>'

        create.footer_box_2_name_en = 'Information'
        create.footer_link_2_1_en = '<a href="http://127.0.0.1:8000/create/" target="_blank">About the author</a>'
        create.footer_link_2_2_en = '<a href="http://127.0.0.1:8000/create/" target="_blank">Instagram</a>'

        # блок текста ru

        create.text_1_ru = 'По всем вопросам обращайтесь по адресу art-sonik@mail.ru или пишите в социальных сетях проекта'
        create.text_2_ru = 'BADBOT 2024'

        # en

        create.text_1_en = 'For any questions, please contact art-sonik@mail.ru or write on the social networks of the project'
        create.text_2_en = 'BADBOT 2024'

        create.link_1 = 'http://127.0.0.1:8000/create/'
        create.icon_1 = 'media/design/icons/instagram.png'

        create.link_2 = 'http://127.0.0.1:8000/create/'
        create.icon_2 = 'media/design/icons/twitter.png'

        create.save()

        # УДАЛИТЬ

        from django.contrib.auth import get_user_model

        User = get_user_model()

        if not User.objects.filter(username='user').exists():
            User.objects.create_superuser('user', 'admin@example.com', '12345')