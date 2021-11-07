from faker import Faker

CM_PER_INC = 2.54
KG_PER_POUND = 0.45


def inch2cm(value):
    return round(value * CM_PER_INC, 2)


def pound2kg(value):
    return round(value * KG_PER_POUND, 2)


def get_students_list():
    f = Faker()
    return [f.name() for _ in range(10)]
