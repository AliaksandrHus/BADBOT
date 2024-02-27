from PIL import Image
from .models import Collection


def create_img(elements, random_list):

    """ Функция создания изображения """

    # картинка 144

    background_144 = Image.open(elements[2].background)
    frame_144 = Image.open(elements[2].frame)
    name1_144 = Image.open(elements[0][0].element1)
    name2_144 = Image.open(elements[0][0].element2)
    antenna_144 = Image.open(elements[0][1].element1)
    eyes_144 = Image.open(elements[0][2].element1)
    mouth_144 = Image.open(elements[0][3].element1)

    name_accessoires_144_1 = False
    name_accessoires_144_2 = False
    eyes_accessoires_144 = False
    mouth_accessoires_144_1 = False
    mouth_accessoires_144_2 = False
    rare_accessoires_144 = False

    if random_list[4] != 0:
        name_accessoires_144_1 = Image.open(elements[0][4].element1)
        if elements[0][4].element2: name_accessoires_144_2 = Image.open(elements[0][4].element2)

    if random_list[5] != 0:
        eyes_accessoires_144 = Image.open(elements[0][5].element1)

    if random_list[6] != 0:
        mouth_accessoires_144_1 = Image.open(elements[0][6].element1)
        if elements[0][6].element2: mouth_accessoires_144_2 = Image.open(elements[0][6].element2)

    if random_list[7] != 0:
        rare_accessoires_144 = Image.open(elements[0][7].element1)

    #

    new_image_db = Collection()

    new_image_db.name_ru = elements[0][0].name_ru
    new_image_db.name_en = elements[0][0].name_en

    new_image_db.antenna_ru = elements[0][1].name_ru
    new_image_db.antenna_en = elements[0][1].name_en

    new_image_db.eyes_ru = elements[0][2].name_ru
    new_image_db.eyes_en = elements[0][2].name_en

    new_image_db.mouth_ru = elements[0][3].name_ru
    new_image_db.mouth_en = elements[0][3].name_en

    if random_list[4] != 0:
        new_image_db.name_accessoires_ru = elements[0][4].name_ru
        new_image_db.name_accessoires_en = elements[0][4].name_en
    else:
        new_image_db.name_accessoires_ru = '-'
        new_image_db.name_accessoires_en = '-'

    if random_list[5] != 0:
        new_image_db.eyes_accessoires_ru = elements[0][5].name_ru
        new_image_db.eyes_accessoires_en = elements[0][5].name_en
    else:
        new_image_db.eyes_accessoires_ru = '-'
        new_image_db.eyes_accessoires_en = '-'

    if random_list[6] != 0:
        new_image_db.mouth_accessoires_ru = elements[0][6].name_ru
        new_image_db.mouth_accessoires_en = elements[0][6].name_en
    else:
        new_image_db.mouth_accessoires_ru = '-'
        new_image_db.mouth_accessoires_en = '-'

    if random_list[7] != 0:
        new_image_db.rare_accessoires_ru = elements[0][7].name_ru
        new_image_db.rare_accessoires_en = elements[0][7].name_en
    else:
        new_image_db.rare_accessoires_ru = '-'
        new_image_db.rare_accessoires_en = '-'

    new_image_db.elements_id = '-'.join([str(x) for x in random_list])

    new_image_db.save()

    #

    mask = name2_144.point(lambda p: p * 100)

    if random_list[6] == 1:
        breads = Image.composite(mouth_accessoires_144_1, frame_144, mask)
        head = Image.alpha_composite(name2_144, breads)
        head = Image.alpha_composite(head, name1_144)
    else: head = Image.alpha_composite(name2_144, name1_144)

    mouth_720 = Image.composite(mouth_144, frame_144, mask)
    head = Image.alpha_composite(head, mouth_720)

    if random_list[5] == 0:
        head = Image.alpha_composite(head, eyes_144)
    elif random_list[5] == 1:
        head = Image.alpha_composite(head, eyes_144)
        head = Image.alpha_composite(head, eyes_accessoires_144)
    else:
        head = Image.alpha_composite(head, eyes_accessoires_144)

    if mouth_accessoires_144_1 and random_list[6] not in [1, 8, 10]:
        if random_list[6] == 3 and random_list[2] == 45:
            head = Image.alpha_composite(head, mouth_accessoires_144_2)
        else: head = Image.alpha_composite(head, mouth_accessoires_144_1)

    if rare_accessoires_144:
        head = Image.alpha_composite(head, rare_accessoires_144)

    if name_accessoires_144_2:
        head = Image.alpha_composite(name_accessoires_144_2, head)

    if mouth_accessoires_144_1 and random_list[6] in [8, 10]:
        head = Image.alpha_composite(head, mouth_accessoires_144_1)

    head = Image.alpha_composite(head, antenna_144)

    if name_accessoires_144_1:
        head = Image.alpha_composite(head, name_accessoires_144_1)

    if random_list[6] == 5 and random_list[7] == 43:
        head = Image.alpha_composite(head, mouth_accessoires_144_1)

    head = Image.alpha_composite(background_144, head)

    width, height = background_144.size
    new_image = Image.new('RGBA', (width, height), color=(255, 255, 255, 0))
    new_image.paste(head, (0, 0), head)
    new_image.save(f'media/image/created/144/144_{new_image_db.image_id}_{new_image_db.elements_id}.png')

    new_image_db.image144 = f'media/image/created/144/144_{new_image_db.image_id}_{new_image_db.elements_id}.png'

    new_image_db.save()

    # картинка 720

    background_720 = Image.open(elements[2].background)
    frame_720 = Image.open(elements[2].frame)
    name1_720 = Image.open(elements[1][0].element1)
    name2_720 = Image.open(elements[1][0].element2)
    name3_720 = Image.open(elements[1][0].element3)
    antenna_720_1 = Image.open(elements[1][1].element1)
    antenna_720_2 = Image.open(elements[1][1].element2) if elements[1][1].element2 else False
    eyes_720 = Image.open(elements[1][2].element1)
    mouth_720 = Image.open(elements[1][3].element1)

    name_accessoires_720_1 = False
    name_accessoires_720_2 = False
    eyes_accessoires_720 = False
    mouth_accessoires_720 = False
    rare_accessoires_720 = False

    if random_list[4] != 0:
        name_accessoires_720_1 = Image.open(elements[1][4].element1)
        if elements[1][4].element2: name_accessoires_720_2 = Image.open(elements[1][4].element2)

    if random_list[5] != 0:
        eyes_accessoires_720 = Image.open(elements[1][5].element1)

    if random_list[6] != 0:
        mouth_accessoires_720 = Image.open(elements[1][6].element1)

    if random_list[7] != 0:
        rare_accessoires_720 = Image.open(elements[1][7].element1)

    #

    mask = name2_720.point(lambda p: p * 100)

    if random_list[6] == 1 or random_list[6] == 5 or random_list[6] == 9:
        breads = Image.composite(mouth_accessoires_720, frame_720, mask)
        head = Image.alpha_composite(name2_720, breads)
        if random_list[6] == 1: head = Image.alpha_composite(head, name3_720)
        head = Image.alpha_composite(head, name1_720)
    else: head = Image.alpha_composite(name2_720, name1_720)

    mouth_720 = Image.composite(mouth_720, frame_720, mask)
    head = Image.alpha_composite(head, mouth_720)

    if mouth_accessoires_720 and random_list[6] != 1 and random_list[6] != 5 and random_list[6] != 9:
        head = Image.alpha_composite(head, mouth_accessoires_720)

    if rare_accessoires_720:
        head = Image.alpha_composite(head, rare_accessoires_720)

    if random_list[1] in [21, 22, 26, 36, 34, 9, 16]:
        antenna = Image.composite(antenna_720_1, frame_720, mask)
        head = Image.alpha_composite(head, antenna)
    else: head = Image.alpha_composite(head, antenna_720_1)

    if random_list[5] == 0:
        head = Image.alpha_composite(head, eyes_720)
    elif random_list[5] == 1:
        head = Image.alpha_composite(head, eyes_720)
        head = Image.alpha_composite(head, eyes_accessoires_720)
    elif random_list[5] == 3:
        pirate = Image.composite(eyes_accessoires_720, frame_720, mask)
        head = Image.alpha_composite(head, pirate)
    else:
        head = Image.alpha_composite(head, eyes_accessoires_720)

    if antenna_720_2:
        head = Image.alpha_composite(antenna_720_2, head)

    if name_accessoires_720_2:
        head = Image.alpha_composite(name_accessoires_720_2, head)

    if name_accessoires_720_1:
        head = Image.alpha_composite(head, name_accessoires_720_1)

    head = Image.alpha_composite(background_720, head)

    width, height = background_720.size
    new_image = Image.new('RGBA', (width, height), color=(255, 255, 255, 0))
    new_image.paste(head, (0, 0), head)
    new_image.save(f'media/image/created/720/720_{new_image_db.image_id}_{new_image_db.elements_id}.png')

    new_image_db.image720 = f'media/image/created/720/720_{new_image_db.image_id}_{new_image_db.elements_id}.png'

    new_image_db.save()

    return new_image_db
