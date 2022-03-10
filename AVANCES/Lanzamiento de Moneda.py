import random

resultados = {'cruz': 0, 'cara': 0}

lados = list(resultados.keys())

for _ in range(1000):
    resultados[random.choice(lados)] += 1

print('Cruz:', resultados['cruz'])
print('Cara:', resultados['cara'])