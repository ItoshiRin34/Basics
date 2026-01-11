def contar_letras(frase):
    contador = {}
    for letra in frase:
        if letra not in contador:
            contador[letra] = 1
        else:
            contador[letra] += 1
    return contador

texto = "banana"
resultado = contar_letras(texto)
print(resultado)
