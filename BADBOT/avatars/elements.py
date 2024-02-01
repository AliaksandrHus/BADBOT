from .models import Name144, Mouth144, Eyes144, Antenna144, \
    NameAccessoires144, EyesAccessoires144, MouthAccessoires144, RareAccessoires144

from .models import Name720, Mouth720, Eyes720, Antenna720, \
    NameAccessoires720, EyesAccessoires720, MouthAccessoires720, RareAccessoires720

from .models import Additionally


def get_elements(random_list):

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
