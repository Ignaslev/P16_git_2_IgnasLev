def kaupk_daugyba(*args: int | float) -> int | float:
    kaupiklis = 1
    for elem in args:
        kaupiklis *= elem

    return kaupiklis


def sudaugink_visus_is_pirmo(skaicius, *args):
    return [skaicius * elem for elem in args]


def gauk_sumas_a(*args: int | float):
    lyginiu_suma = 0
    nelyginiu_suma = 0

    for num in args:
        if num % 2 == 0:
            lyginiu_suma += num
        else:
            nelyginiu_suma += num
    return (lyginiu_suma, nelyginiu_suma)


def gauk_sumas_b(*args: int | float, info=False):
    lyginiu_suma = 0
    nelyginiu_suma = 0
    lyginiai_skaiciai = []
    nelyfiniai_skaiciai = []

    for num in args:
        if num % 2 == 0:
            lyginiu_suma += num
            lyginiai_skaiciai.append(num)
        else:
            nelyginiu_suma += num
            nelyfiniai_skaiciai.append(num)

    if info:
        return (f'Visi skaiciai: {args},'
                f'lyginiai skaiciai: {lyginiai_skaiciai}, '
                f'nelyginiai skaiciai: {nelyfiniai_skaiciai}, '
                f'lyginiu suma: {lyginiu_suma}, '
                f'nelyginiu suma: {nelyginiu_suma}')

    else:
        return (lyginiu_suma, nelyginiu_suma)


def gauk_sumas_c(*args: int | float):
    lyginiu_suma = 0
    nelyginiu_suma = 0
    lyginiai_skaiciai = []
    nelyfiniai_skaiciai = []
    for num in args:
        if num % 2 == 0:
            lyginiu_suma += num
            lyginiai_skaiciai.append(num)
        else:
            nelyginiu_suma += num
            nelyfiniai_skaiciai.append(num)

    return {
        'Visi skaiciai': args,
        'lyginiai skaiciai': lyginiai_skaiciai,
        'nelyginiai skaiciai': nelyfiniai_skaiciai,
        'lyginiu suma': lyginiu_suma,
        'nelyginiu suma': nelyginiu_suma,
        'dydziausias skaicius': max(args),
        'maziausias skaicius': min(args)
    }


def kaupk_aritmetika(*args, operacija='suma'):
    suma = 0
    atimtis = args[0]
    dalyba = args[0]
    daugyba = args[0]

    if len(args) == 0:
        return 0
    if len(args) == 1:
        return args[0]

    if operacija == 'suma':
        for number in args:
            suma += number
        return suma

    if operacija == 'atimtis':
        for number in args[1:]:
            atimtis -= number
        return atimtis

    if operacija == 'dalyba':
        for number in args[1:]:
            dalyba /= number
        return dalyba

    if operacija == 'daugyba':
        for number in args[1:]:
            daugyba *= number
        return daugyba


def filtruok_stringus_a(*args: str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    stringai = []
    for text in args:
        if text.lower()[0] in vowels:
            stringai.append(text)
    return stringai


def filtruok_stringus_b(*args: str, lt=False):
    stringai = []
    if lt:
        vowels = ['a', 'ą', 'e', 'ę', 'ė', 'i', 'į', 'o', 'u', 'ų', 'ū', 'y']
        for text in args:
            if text.lower()[0] in vowels:
                stringai.append(text)

    else:
        vowels = ['a', 'e', 'i', 'o', 'u']
        for text in args:
            if text.lower()[0] in vowels:
                stringai.append(text)
    return stringai


def check_autonr_a(text: str):
    if len(text) != 6:
        return False
    if text[0:3].isalpha() and text[3:].isdigit():
        return True
    else:
        return False


def check_autonr_b(text: str, elektro=False):
    if len(text) != 6:
        return False
    if elektro:
        if text[0] == 'E' and text[0:2].isalpha() and text[2:].isdigit():
            return True
        else:
            return False
    if text[0:3].isalpha() and text[3:].isdigit():
        return True
    else:
        return False


def check_autonrs_a(*args: str):
    tinkami_numeriai = []

    for plate in args:
        if len(plate) != 6:
            continue
        if plate[0:3].isalpha() and plate[3:].isdigit():
            tinkami_numeriai.append(plate)
        if plate[0] == 'E' and plate[0:2].isalpha() and plate[2:].isdigit():
            tinkami_numeriai.append(plate)
    return tinkami_numeriai


def check_autonrs_b(*args: str, **kwargs):
    tinkami_numeriai = []
    for plate in args:
        if len(plate) != 6:
            continue
        if plate[0:3].isalpha() and plate[3:].isdigit():
            tinkami_numeriai.append(plate)
        if plate[0] == 'E' and plate[0:2].isalpha() and plate[2:].isdigit():
            tinkami_numeriai.append(plate)

    return sorted(tinkami_numeriai, **kwargs)
