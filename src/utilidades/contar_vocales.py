def contar_vocales(i):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in i if letra in vocales)


