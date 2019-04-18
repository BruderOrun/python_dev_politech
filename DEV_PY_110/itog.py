import random
import re
import logging
import os.path
import json

country = 'Russia'

city = 'Magadan'

street = ['11ya.Repina', 'Zarubina', 'Harbinskaya', 'Runnays']


def check(country, city, street):
    template = re.compile(r'..\D+')
    assert type(country) == str and template.fullmatch(country), '.contry.'
    assert type(city) == str and template.fullmatch(city), '.city.'
    street = set(street)
    street_val = [i for i in street if template.fullmatch(i)]
    assert len(street) == len(street_val), 'Потеряли улицу, не допустимый формат'

    return country, city, street


check(country, city, street)


def gener(funk):
    def gen(*args, **kwargs):
        for i in args:
            if i == 'test':
                logging.warning(f'{funk.__name__} vot ono, вы попали на реальные данные')
                quit()
        return funk(*args, **kwargs)

    return gen


@gener
def super_gen(country, city, street):
    house = random.randint(1, 40)
    street = random.choice(street)
    korp = None if house <= 15 else random.randint(1, 8)
    while True:
        yield \
            country, city, street, house, korp


g = super_gen(country, city, street)
g.send(None)


def writing_data_json():
    file = '/Users/norunov/Desktop/python/data.txt'
    if os.path.isfile(file) == False:
        with open(file, "w") as write_file:
            json.dump(next(g), write_file)
    else:
        with open(file, "w") as write_file:
            json.dump(next(g), write_file)


def reading(file='/Users/norunov/Desktop/python/data.txt'):
    with open(file, "r") as write_file:
        print(write_file.read())


if __name__ == '__main__':
    check(country, city, street)
    super_gen(country, city, street)
    logging.warning(next(g))
    writing_data_json()
    reading(file='/Users/norunov/Desktop/python/data.txt')
