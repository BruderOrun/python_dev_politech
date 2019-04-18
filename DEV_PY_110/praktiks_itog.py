import  random

country = 'RF'
city = 'Sankt-Peterburg'
street = ['Парковая', 'Науки', 'Мира', 'Захадум', 'Варварская', 'Netaaaaa']

run = random.choice(street)
print(run)


def coro(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner