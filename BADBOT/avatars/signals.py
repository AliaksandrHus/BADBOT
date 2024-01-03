from django.db.models.signals import post_migrate
from django.dispatch import receiver
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

