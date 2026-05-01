'''
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

def fizzbuzz ():

    for n in range(1, 101): # Recorre n en un rango de 1 a 100
        mul_3 = n % 3 == 0 # Si el residuo de n entre 3 es 0, True de lo contrario False
        mul_5 = n % 5 == 0 # Si el residuo de n entre 5 es 0, True de lo contrario False

        if mul_3 and mul_5: # Si mul_3 es True y mul_5 es True, imprime fizzbuzz (Tablas de verdad)
            print(f"{n}: fizzbuzz")

        elif mul_3: # Si mul_3 es True, imprime fizz
            print(f"{n}: fizz")

        elif mul_5: # Si mul_5 es True, imprime buzz
            print(f"{n}: buzz")

        else: print(n) # Si no cumple, imprime el número.


fizzbuzz()