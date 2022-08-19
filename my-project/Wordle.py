import random
from termcolor import colored

class Instrucciones:
    
    def _init__(self):
        pass
    
    def instruc_juego(self):
        print( """En este juego tienes que adivinar una palabra oculta de cinco letras. Tienes seis intentos. 

 – Si la palabra que escribiste tiene alguna letra en la posición corrrecta, ✅ este emoji aparecerá en pantalla.

 – Si hay alguna letra que pertenece a la palabra oculta pero no está en la posición correcta, entonces aparecerá 🔥. 

 – Finalmente, si la palabra tiene alguna letra que no pertenece a la palabra oculta, entonces te marcará ❌.

NOTA: En cualquier momnento puedes obtener un hint si así lo deseas, pero ten en cuenta que esto te descontará un intento del total de intentos que tienes. Para obtener un hint sólo escribe "hint". Además, también puedes escribir "me rindo" y automáticamente el juego terminará y podrás conocer la palabra oculta.

""")

class Juego:
    
    def __init__(self):
        pass
    
    def nombre(self):
        nombre_jugador = input('¡Hola! ¿Cuál es tu nombre? ')
        return f'Perfecto. ¿List@ para empezar, {nombre_jugador}? Vamos allá!'
    
    def jugar(self):
        lista_de_palabras = ['bolsa', 'hotel', 'katia', 'sismo', 'peras', 'oliva', 'polos', 
                            'añade', 'clave', 'cerca', 'parte', 'buena']
        
        hints = ['saco', 'hostal', 'estudiante de Ironhack', 'temblor', "'o...o manzanas'", "aceite de...", "'...opuestos'", 
                'él/ella suma', 'llave, cifra', '=! lejos', "pedazo", 'bondadosa']
        n_intento = 6
        palabra_random = random.choice(lista_de_palabras)
        #indice = lista_de_palabras[palabra_random] 
        ## El while lo uso aquí porque el proceso se va a ejecutar hasta que el usuario adivine 
        ## la palabra correcta o ya no tenga más intentos.
        while n_intento > 0:
            intento = input("Adivina la palabra de 5 letras: ")
            if intento.lower() == "me rindo":
                print("La palabra secreta era", colored(palabra_random.upper(), attrs=['bold']))
                break
            elif intento.lower() == 'hint':
                confirmar = input('¿Estás seguro de querer obtener un hint? Perderás un intento si lo haces. Escribe "s" si quieres obtener un hint o "n" si prefieres seguir sin un hint.')
                if confirmar == 's':
                    n_intento -= 1
                    for i, r in zip(lista_de_palabras, hints):
                        if i == palabra_random:
                            print('Aquí tienes tu hint:', colored(r.upper(), attrs=['bold']), '.', f'Te quedan {n_intento} intento(s).')
                elif confirmar == 'n':
                    intento
            elif len(intento) != len(palabra_random):
                print("Asegúrate de haber escrito una palabra de 5 letras.")
            elif intento.lower() == palabra_random:
                print(colored("¡¡Adivinaste la palabra!! YUJUU! 🥳", attrs=['bold']))
                break
            else:
                n_intento -= 1
                print(f"Sigue jugando. Te quedan {n_intento} intento(s).")
                for i, r in zip(intento, palabra_random):
                    if i == r:
                        print(i, '✅')
                    elif i in palabra_random:
                        print(i, '🔥')
                    else:
                        print(i, '❌')
                if n_intento == 0:
                    print("Suerte para la próxima vez!!!! ")
                    print('La palabra correcta era:', colored(palabra_random.upper(), attrs=['bold']))
       