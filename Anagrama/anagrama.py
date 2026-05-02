'''
Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) 
según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS
   las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.
'''

def es_Anagrama (world_1, world_2):
    w1 = sorted(world_1.lower().replace(" ", ""))
    w2 = sorted(world_2.lower().replace(" ", ""))

    if w1 == w2: return "Verdadero"
    else: return "Falso"

print("=" * 30)
print("\t¿ES ANAGRAMA?")
print("=" * 30)

palabra1 = input("Ingresa la palabra 1: ")
palabra2 = input("Ingresa la palabra 2: ")

print(f"Es {es_Anagrama(palabra1, palabra2)}")