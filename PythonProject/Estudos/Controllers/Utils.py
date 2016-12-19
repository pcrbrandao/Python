# encoding: utf-8
def imprime_quadrados():
    quadrados = []
    for x in range(10):
        quadrados.append(x**2)
    print(quadrados)

def imprime_colunas(intervalo):
    for x in intervalo:
        print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

def reverse(data):
    intervalo = range(len(data)-1, -1, -1)
    print(intervalo)

    for index in intervalo:
        yield data[index]

def print_reverse(data):
    for char in reverse(data):
        print(char, end='')

def greeting(name: str) -> str:
    return 'Olá ' + name