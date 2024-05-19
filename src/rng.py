from datetime import datetime
waktu_saat_ini = datetime.now()
detik = (waktu_saat_ini - datetime(2024, 5, 17)).total_seconds()//1
def lcg(x, a, c, m):
    while True:
        x = (a * x + c) % m
        yield x


def random_uniform_sample(batas, seed=detik):
    interval = [0, batas]
    a, c, m = 1103515245, 12345, 2 ** 31
    bsdrand = lcg(seed, a, c, m)

    lower, upper = interval[0], interval[1]
    observation = (upper - lower) * (next(bsdrand) / (2 ** 31 - 1)) + lower

    return round(observation)