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


# Модель контента

class Content(models.Model):
    """Модель контента"""

    id = models.IntegerField(primary_key=True)

    # контент index

    index_text_1_ru = models.TextField('Текст Index RU №1', blank=True)
    index_text_2_ru = models.TextField('Текст Index RU №2', blank=True)

    index_text_1_en = models.TextField('Текст Index EN №1', blank=True)
    index_text_2_en = models.TextField('Текст Index EN №2', blank=True)

    index_img_1 = models.ImageField('Картинка Index №1', upload_to='media/design/content/', blank=True)
    index_img_2 = models.ImageField('Картинка Index №2', upload_to='media/design/content/', blank=True)
    index_img_3 = models.ImageField('Картинка Index №3', upload_to='media/design/content/', blank=True)
    index_img_4 = models.ImageField('Картинка Index №4', upload_to='media/design/content/', blank=True)
    index_img_5 = models.ImageField('Картинка Index №5', upload_to='media/design/content/', blank=True)

    # контент create

    create_text_1_ru = models.TextField('Контент Create RU №1', blank=True)
    create_text_2_ru = models.TextField('Контент Create RU №2', blank=True)

    create_text_1_en = models.TextField('Контент Create EN №1', blank=True)
    create_text_2_en = models.TextField('Контент Create EN №2', blank=True)

    create_img_1 = models.ImageField('Картинка Create №1', upload_to='media/design/content/', blank=True)
    create_img_2 = models.ImageField('Картинка Create №2', upload_to='media/design/content/', blank=True)
    create_img_3 = models.ImageField('Картинка Create №3', upload_to='media/design/content/', blank=True)
    create_img_4 = models.ImageField('Картинка Create №4', upload_to='media/design/content/', blank=True)
    create_img_5 = models.ImageField('Картинка Create №5', upload_to='media/design/content/', blank=True)

    # контент collection

    collection_text_1_ru = models.TextField('Контент Collection RU №1', blank=True)
    collection_text_2_ru = models.TextField('Контент Collection RU №2', blank=True)

    collection_text_1_en = models.TextField('Контент Collection EN №1', blank=True)
    collection_text_2_en = models.TextField('Контент Collection EN №2', blank=True)

    collection_img_1 = models.ImageField('Картинка Collection №1', upload_to='media/design/content/', blank=True)
    collection_img_2 = models.ImageField('Картинка Collection №2', upload_to='media/design/content/', blank=True)
    collection_img_3 = models.ImageField('Картинка Collection №3', upload_to='media/design/content/', blank=True)
    collection_img_4 = models.ImageField('Картинка Collection №4', upload_to='media/design/content/', blank=True)
    collection_img_5 = models.ImageField('Картинка Collection №5', upload_to='media/design/content/', blank=True)

    # объявление

    index_message_ru = models.TextField('Объявление Index RU', blank=True)
    index_message_en = models.TextField('Объявление Index EN', blank=True)

    create_message_ru = models.TextField('Объявление Create RU', blank=True)
    create_message_en = models.TextField('Объявление Create EN', blank=True)

    collection_message_ru = models.TextField('Объявление Collection RU', blank=True)
    collection_message_en = models.TextField('Объявление Collection en', blank=True)


# Модель футера

class Footer(models.Model):
    """Модель футера"""

    id = models.IntegerField(primary_key=True)

    # блок №1 ru

    footer_box_1_name_ru = models.TextField('Заголовок блока #1 RU', blank=True, max_length=50)

    footer_link_1_1_ru = models.TextField('Ссылка 1 блока #1 RU', blank=True)
    footer_link_1_2_ru = models.TextField('Ссылка 2 блока #1 RU', blank=True)
    footer_link_1_3_ru = models.TextField('Ссылка 3 блока #1 RU', blank=True)
    footer_link_1_4_ru = models.TextField('Ссылка 4 блока #1 RU', blank=True)
    footer_link_1_5_ru = models.TextField('Ссылка 5 блока #1 RU', blank=True)
    footer_link_1_6_ru = models.TextField('Ссылка 6 блока #1 RU', blank=True)

    # en

    footer_box_1_name_en = models.TextField('Заголовок блока #1 EN', blank=True, max_length=50)

    footer_link_1_1_en = models.TextField('Ссылка 1 блока #1 EN', blank=True)
    footer_link_1_2_en = models.TextField('Ссылка 2 блока #1 EN', blank=True)
    footer_link_1_3_en = models.TextField('Ссылка 3 блока #1 EN', blank=True)
    footer_link_1_4_en = models.TextField('Ссылка 4 блока #1 EN', blank=True)
    footer_link_1_5_en = models.TextField('Ссылка 5 блока #1 EN', blank=True)
    footer_link_1_6_en = models.TextField('Ссылка 6 блока #1 EN', blank=True)

    # блок №2 ru

    footer_box_2_name_ru = models.TextField('Заголовок блока #2 RU', blank=True, max_length=50)

    footer_link_2_1_ru = models.TextField('Ссылка 1 блока #2 RU', blank=True)
    footer_link_2_2_ru = models.TextField('Ссылка 2 блока #2 RU', blank=True)
    footer_link_2_3_ru = models.TextField('Ссылка 3 блока #2 RU', blank=True)
    footer_link_2_4_ru = models.TextField('Ссылка 4 блока #2 RU', blank=True)
    footer_link_2_5_ru = models.TextField('Ссылка 5 блока #2 RU', blank=True)
    footer_link_2_6_ru = models.TextField('Ссылка 6 блока #2 RU', blank=True)

    # en

    footer_box_2_name_en = models.TextField('Заголовок блока #2 EN', blank=True, max_length=50)

    footer_link_2_1_en = models.TextField('Ссылка 1 блока #2 EN', blank=True)
    footer_link_2_2_en = models.TextField('Ссылка 2 блока #2 EN', blank=True)
    footer_link_2_3_en = models.TextField('Ссылка 3 блока #2 EN', blank=True)
    footer_link_2_4_en = models.TextField('Ссылка 4 блока #2 EN', blank=True)
    footer_link_2_5_en = models.TextField('Ссылка 5 блока #2 EN', blank=True)
    footer_link_2_6_en = models.TextField('Ссылка 6 блока #2 EN', blank=True)

    # блок №3 ru

    footer_box_3_name_ru = models.TextField('Заголовок блока #3 RU', blank=True, max_length=50)

    footer_link_3_1_ru = models.TextField('Ссылка 1 блока #3 RU', blank=True)
    footer_link_3_2_ru = models.TextField('Ссылка 2 блока #3 RU', blank=True)
    footer_link_3_3_ru = models.TextField('Ссылка 3 блока #3 RU', blank=True)
    footer_link_3_4_ru = models.TextField('Ссылка 4 блока #3 RU', blank=True)
    footer_link_3_5_ru = models.TextField('Ссылка 5 блока #3 RU', blank=True)
    footer_link_3_6_ru = models.TextField('Ссылка 6 блока #3 RU', blank=True)

    # en

    footer_box_3_name_en = models.TextField('Заголовок блока #3 EN', blank=True, max_length=50)

    footer_link_3_1_en = models.TextField('Ссылка 1 блока #3 EN', blank=True)
    footer_link_3_2_en = models.TextField('Ссылка 2 блока #3 EN', blank=True)
    footer_link_3_3_en = models.TextField('Ссылка 3 блока #3 EN', blank=True)
    footer_link_3_4_en = models.TextField('Ссылка 4 блока #3 EN', blank=True)
    footer_link_3_5_en = models.TextField('Ссылка 5 блока #3 EN', blank=True)
    footer_link_3_6_en = models.TextField('Ссылка 6 блока #3 EN', blank=True)

    # строка с текстом ru

    text_1_ru = models.TextField('Текст #1 RU', blank=True)
    text_2_ru = models.TextField('Текст #2 RU', blank=True)

    # en

    text_1_en = models.TextField('Текст #1 EN', blank=True)
    text_2_en = models.TextField('Текст #2 EN', blank=True)

    # иконки ссылки

    link_1 = models.TextField('Ссылка #1', blank=True)
    icon_1 = models.ImageField('Иконка #1', upload_to='media/design/icons/', blank=True)

    link_2 = models.TextField('Ссылка #2', blank=True)
    icon_2 = models.ImageField('Иконка #2', upload_to='media/design/icons/', blank=True)

    link_3 = models.TextField('Ссылка #3', blank=True)
    icon_3 = models.ImageField('Иконка #3', upload_to='media/design/icons/', blank=True)

    link_4 = models.TextField('Ссылка #4', blank=True)
    icon_4 = models.ImageField('Иконка #4', upload_to='media/design/icons/', blank=True)

    link_5 = models.TextField('Ссылка #5', blank=True)
    icon_5 = models.ImageField('Иконка #5', upload_to='media/design/icons/', blank=True)

    link_6 = models.TextField('Ссылка #6', blank=True)
    icon_6 = models.ImageField('Иконка #6', upload_to='media/design/icons/', blank=True)
