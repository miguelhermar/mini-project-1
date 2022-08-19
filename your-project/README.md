<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Mini Project 1 - Build your own game (Wordle)
*Miguel Ángel Hernández Márquez*

*Agosto 2022, México, 19 de agosto*

## Contenido
- [Descripción del juego](#descripción-del-juego)
- [Reglas](#reglas)
- [Organización](#organización)
- [Links](#links)

## Descripción del juego
El juego se trata de adivinar una palabra de cinco letras en seis intentos.

1. Usaremos una lista de palabras con cinco letras y escogeremos una al azar que sea la palabra oculta.
2. El usuario tendrá que adivinar la palabra oculta durante 6 intentos.
3. Crearemos una variable que almacene el número de veces que el usuario intenta adivinar la palabra.
4. Necesitamos también un condicional para cada uno de los resultados que arroje el input del usuario.
    
## Reglas
- Si una letra se adivina correctamente y en la posición correcta --> ✅
     
- Si se adivina una letra correctamente pero está en la posición incorrecta --> 🔥
     
- Si una letra no está en la palabra oculta --> ❌

En cualquier momnento el usuario puede obtener un hint si así lo desea, pero esto le descontará un intento del total de intentos que tiene. Para obtener un hint se necesita escribir "hint" en el prompt. Además, el usuario también puede escribir "me rindo" y automáticamente el juego terminará y podrá conocer la palabra oculta.


## Organización
Para este juego utilizo una archivo de python (Wordle.py) donde están contenidas las clases del juego (Instrucciones y Juego) y sus funciones. Estas clases las importo en el jupyter notebook donde tendrá lugar el juego en sí. 

## Links

[Repository](https://github.com/)  
[Slides](https://slides.com/)  
[Trello](https://trello.com/en)  
