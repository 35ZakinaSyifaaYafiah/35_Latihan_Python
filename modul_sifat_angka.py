import math

def cek_status_prima(bilangan):
    if bilangan <= 1:
        return False
    for i in range(2, int(math.isqrt(bilangan)) + 1):
        if bilangan % i == 0:
            return False
    return True

def cek_paritas_bilangan(bilangan):
    if bilangan % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"
