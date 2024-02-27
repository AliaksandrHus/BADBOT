from django.db import models

# Модель BADBOT 144


class Name144(models.Model):
    """Модель элемента - имя"""

    id = models.IntegerField(primary_key=True)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    element1 = models.ImageField(upload_to='elements/name/')
    element2 = models.ImageField(upload_to='elements/name/')


class Mouth144(models.Model):
    """Модель элемента - рот"""

    id = models.IntegerField(primary_key=True)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    element1 = models.ImageField(upload_to='elements/name/')
    element2 = models.ImageField(upload_to='elements/name/')


class Eyes144(models.Model):
    """Модель элемента - глаза"""

    id = models.IntegerField(primary_key=True)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    element1 = models.ImageField(upload_to='elements/name/')
    element2 = models.ImageField(upload_to='elements/name/')


class Antenna144(models.Model):
    """Модель элемента - антенна"""

    id = models.IntegerField(primary_key=True)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    element1 = models.ImageField(upload_to='elements/name/')
    element2 = models.ImageField(upload_to='elements/name/')


class MouthAccessoires144(models.Model):
    """Модель элемента - аксессуары рта"""

    id = models.IntegerField(primary_key=True)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    element1 = models.ImageField(upload_to='elements/name/')
    element2 = models.ImageField(upload_to='elements/name/')


class EyesAccessoires144(models.Model):
    """Модель элемента - аксессуары глаз"""

    id = models.IntegerField(primary_key=True)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    element1 = models.ImageField(upload_to='elements/name/')
    element2 = models.ImageField(upload_to='elements/name/')


class NameAccessoires144(models.Model):
    """Модель элемента - аксессуары головы"""

    id = models.IntegerField(primary_key=True)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    element1 = models.ImageField(upload_to='elements/name/')
    element2 = models.ImageField(upload_to='elements/name/')


class RareAccessoires144(models.Model):
    """Модель элемента - аксессуары редкие"""

    id = models.IntegerField(primary_key=True)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    element1 = models.ImageField(upload_to='elements/name/')
    element2 = models.ImageField(upload_to='elements/name/')


# Модель BADBOT 720

class Name720(models.Model):
    """Модель элемента - имя"""

    id = models.IntegerField(primary_key=True)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    element1 = models.ImageField(upload_to='elements/name/')
    element2 = models.ImageField(upload_to='elements/name/')
    element3 = models.ImageField(upload_to='elements/name/')


class Mouth720(models.Model):
    """Модель элемента - рот"""

    id = models.IntegerField(primary_key=True)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    element1 = models.ImageField(upload_to='elements/name/')
    element2 = models.ImageField(upload_to='elements/name/')


class Eyes720(models.Model):
    """Модель элемента - глаза"""

    id = models.IntegerField(primary_key=True)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    element1 = models.ImageField(upload_to='elements/name/')
    element2 = models.ImageField(upload_to='elements/name/')


class Antenna720(models.Model):
    """Модель элемента - антенна"""

    id = models.IntegerField(primary_key=True)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    element1 = models.ImageField(upload_to='elements/name/')
    element2 = models.ImageField(upload_to='elements/name/')


class MouthAccessoires720(models.Model):
    """Модель элемента - аксессуары рта"""

    id = models.IntegerField(primary_key=True)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    element1 = models.ImageField(upload_to='elements/name/')
    element2 = models.ImageField(upload_to='elements/name/')


class EyesAccessoires720(models.Model):
    """Модель элемента - аксессуары глаз"""

    id = models.IntegerField(primary_key=True)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    element1 = models.ImageField(upload_to='elements/name/')
    element2 = models.ImageField(upload_to='elements/name/')


class NameAccessoires720(models.Model):
    """Модель элемента - аксессуары головы"""

    id = models.IntegerField(primary_key=True)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    element1 = models.ImageField(upload_to='elements/name/')
    element2 = models.ImageField(upload_to='elements/name/')


class RareAccessoires720(models.Model):
    """Модель элемента - аксессуары редкие"""

    id = models.IntegerField(primary_key=True)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    element1 = models.ImageField(upload_to='elements/name/')
    element2 = models.ImageField(upload_to='elements/name/')


# Модель дополнительных элементов

class Additionally(models.Model):
    """Модель дополнительных элементов"""

    id = models.IntegerField(primary_key=True)
    background = models.ImageField(upload_to='elements/name/')
    frame = models.ImageField(upload_to='elements/name/')


# Модель готовых ботов

class Collection(models.Model):
    """Модель готовых ботов"""

    image_id = models.AutoField(primary_key=True)
    elements_id = models.CharField(max_length=100)

    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)

    mouth_ru = models.CharField(max_length=100)
    mouth_en = models.CharField(max_length=100)

    eyes_ru = models.CharField(max_length=100)
    eyes_en = models.CharField(max_length=100)

    antenna_ru = models.CharField(max_length=100)
    antenna_en = models.CharField(max_length=100)

    name_accessoires_ru = models.CharField(max_length=100)
    name_accessoires_en = models.CharField(max_length=100)

    mouth_accessoires_ru = models.CharField(max_length=100)
    mouth_accessoires_en = models.CharField(max_length=100)

    eyes_accessoires_ru = models.CharField(max_length=100)
    eyes_accessoires_en = models.CharField(max_length=100)

    rare_accessoires_ru = models.CharField(max_length=100)
    rare_accessoires_en = models.CharField(max_length=100)

    date = models.DateTimeField(auto_now_add=True)

    image144 = models.ImageField(upload_to='elements/name/')
    image720 = models.ImageField(upload_to='elements/name/')


class Content(models.Model):
    """Модель контента"""

    id = models.IntegerField(primary_key=True)

    # контент index

    index_text_1 = models.TextField('Текст Index №1', blank=True)
    index_text_2 = models.TextField('Текст Index №2', blank=True)

    index_img_1 = models.ImageField('Картинка Index №1', upload_to='media/design/content/', blank=True)
    index_img_2 = models.ImageField('Картинка Index №2', upload_to='media/design/content/', blank=True)
    index_img_3 = models.ImageField('Картинка Index №3', upload_to='media/design/content/', blank=True)
    index_img_4 = models.ImageField('Картинка Index №4', upload_to='media/design/content/', blank=True)
    index_img_5 = models.ImageField('Картинка Index №5', upload_to='media/design/content/', blank=True)

    # контент create

    create_text_1 = models.TextField('Контент Create №1', blank=True)
    create_text_2 = models.TextField('Контент Create №2', blank=True)

    create_img_1 = models.ImageField('Картинка Create №1', upload_to='media/design/content/', blank=True)
    create_img_2 = models.ImageField('Картинка Create №2', upload_to='media/design/content/', blank=True)
    create_img_3 = models.ImageField('Картинка Create №3', upload_to='media/design/content/', blank=True)
    create_img_4 = models.ImageField('Картинка Create №4', upload_to='media/design/content/', blank=True)
    create_img_5 = models.ImageField('Картинка Create №5', upload_to='media/design/content/', blank=True)

    # контент collection

    collection_text_1 = models.TextField('Контент Collection №1', blank=True)
    collection_text_2 = models.TextField('Контент Collection №2', blank=True)

    collection_img_1 = models.ImageField('Картинка Collection №1', upload_to='media/design/content/', blank=True)
    collection_img_2 = models.ImageField('Картинка Collection №2', upload_to='media/design/content/', blank=True)
    collection_img_3 = models.ImageField('Картинка Collection №3', upload_to='media/design/content/', blank=True)
    collection_img_4 = models.ImageField('Картинка Collection №4', upload_to='media/design/content/', blank=True)
    collection_img_5 = models.ImageField('Картинка Collection №5', upload_to='media/design/content/', blank=True)

    # объявление

    index_message = models.TextField('Объявление Index', blank=True)
    create_message = models.TextField('Объявление Create', blank=True)
    collection_message = models.TextField('Объявление Collection', blank=True)
