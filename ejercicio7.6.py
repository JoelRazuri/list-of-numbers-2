"""
    Dada una lista de números enteros y un entero k, escribir una función que:
        a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a k.
        b) Devuelva una lista con aquellos que son múltiplos de k.
"""

def listas_mayores_menores_iguales(lista, k):

    num_menores = []
    num_mayores = []
    num_iguales = []

    for num in lista:

        if num == k:
            num_iguales.append(num)
        elif num > k:
            num_mayores.append(num)
        else:
            num_menores.append(num)

    return num_menores, num_iguales, num_mayores


# print(listas_mayores_menores_iguales([1,2,3,3,5,6,3,5,5,10,203,4,53],5))

def lista_multiplos(lista,k):

    num_multiplos = []

    for num in lista:
        if num%k == 0:
            num_multiplos.append(num)

    return num_multiplos


# print(lista_multiplos([10,8,2,1,3,7,23,25],5))

