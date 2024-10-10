def contar_words(palabras):
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

palabras = ["python", "java", "python", "c++"]
print(f"Ejercicio 1: {contar_words(palabras)}")

def combina_diccionarios(dic1, dic2):
    combinado = dic1.copy()
    for cla, val in dic2.items():
        combinado [cla] = combinado.get(cla , 0) + val
    return combinado

dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}
print(f"Ejercicio 2: {combina_diccionarios(dic1, dic2)}")

def listas_frecuencia(numeros):
    frecuencia = {}
    for numeros in numeros:
            frecuencia[numeros] = frecuencia.get(numeros, 0) +1
    return frecuencia
numeros = [1, 1, 2, 3, 3, 3]
print(f"Ejercicio 2: {listas_frecuencia(numeros)}")
# Salida: {1: 2, 2: 1, 3: 3}

def filtar_palabras_larg(palabras, longitud):
     return[palabra for palabra in  palabras if len(palabra) > longitud]
palabras_largas = ["hola", "mundo", "python", "programación"]
longitud = 5
print(f"Ejercicio 4: {filtar_palabras_larg(palabras_largas, longitud)}")

def inv_words(tup):
     return[(w, z) for z, w in tup]
# Ejemplo del Ejercicio 5:
tuplas = [(1, 2), (3, 4), (5, 6)]
print(f"Ejercicio 5: {inv_words(tuplas)}")

def valor_mas_frecuente(lista):
    frecuencia = {}
    
    for num in lista:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num] = 1
    
    valor_frecuente = max(frecuencia, key=frecuencia.get)
    return valor_frecuente

numeros = [1, 2, 3, 1, 2, 1]
print(f"Ejercicio 6: El valor mas frecuiente es {valor_mas_frecuente(numeros)}")  # Salida: 1

def aplanar_lista(lista_de_listas):
    return [elemento for sublista in lista_de_listas for elemento in sublista]

lista_de_listas = [[1, 2], [3, 4], [5]]
# Salida: [1, 2, 3, 4, 5]
resultado = aplanar_lista(lista_de_listas)
print(f"Ejercicio 11 : {(resultado)}")  

def calcular_mediana(numeros):
    n = len(numeros)
    numeros_ordenados = sorted(numeros)  # Ordenamos los números usando sorted()

    if n % 2 == 1:
        return numeros_ordenados[n // 2]
    else:
        return (numeros_ordenados[n // 2 - 1] + numeros_ordenados[n // 2]) / 2

numeros = [1, 3, 2, 4, 5]
result = calcular_mediana(numeros)
print(f"Ejercicio 12 :El resultado es {result}")

def duplicar_elementos(numeros):
    nueva_lista = []
    for num in numeros:
        nueva_lista.append(num)
        nueva_lista.append(num)
    return nueva_lista

# Ejemplo
numeros = [1, 2, 3]
print("Ejercicio 13 : {duplicar_elementos(numeros)}")  # Salida: [1, 1, 2, 2, 3, 3]

def contar_palabras(frases):
    conteo = {}
    for i, frase in enumerate(frases):
        conteo[i] = len(frase.split())
    return conteo

# Ejemplo
frases = ["Hola mundo", "Python es genial", "Me gusta programar"]
print(f"Ejercicio 14 : {contar_palabras(frases)}")  # Salida: {0: 2, 1: 3, 2: 3}

def clave_maxima(diccionario):
    return max(diccionario, key=diccionario.get)

# Ejemplo
diccionario = {'a': 10, 'b': 20, 'c': 5}
print(f"Ejercicio 15 : {clave_maxima(diccionario)}")  # Salida: 'b'

def encontrar_palindromos(palabras):
    palindromos = [palabra for palabra in palabras if palabra == palabra[::-1]]
    return palindromos

# Ejemplo
palabras = ["ana", "oso", "hola", "level"]
print(f"Ejercicio 16 : {encontrar_palindromos(palabras)}")  # Salida: ["ana", "oso", "level"]
