# -*- coding: utf-8 -*-
import random, os

'''
Leer de un archivo
Poner un menu
Poner música
Poner ayuda
Poner letras grandes
Poner un escenario
Ponerlo Web
Ir desplegando la cosas en camara lenta
'''

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

#debe venir desde un archivo de texto
WORDS = [
    'cocolo',
    'papala'
]

def display(RandonWord,Guessed, Tries):
    os.system("cls")
    LongWord = len(RandonWord)
    print(IMAGES[Tries])
    print("" * 2)
    print("PALABRA PARA ADIVINAR:")
    print("--- * --- " * LongWord)
    print("" * 2)
    print(Guessed)
    print("" * 2)
    print("--- * --- " * LongWord)
    print("Cantidad de intentos: {}".format(Tries))   

def FoundChar(RandonWord,Guessed, UserInput):
    Found = False
    for x in range(len(RandonWord)):
        if RandonWord[x] == UserInput and Guessed[x] == "*":
            Guessed[x] = UserInput
            Found = True
            break
    if Found:
        return True
    else:
        return False        

def gano(RandonWord, Guessed):
    Resultado = True
    for x in range(len(RandonWord)):
        if Guessed[x] != RandonWord[x]: Resultado = False 
    return Resultado

def random_word():
    return random.choice(WORDS)

def game():
    RandonWord = random_word() #Es la palabra que se debe adivinar
    Tries = 0 #Son los intentos por adivinar (3). Se resetea si adivina el caracter correcto
    Guessed = ["*"] * len(RandonWord) #Los caracteres adivinados. Lo usaré para ir desplegando
    UserInput = '/' #El caracter que el usuario introduce
   
    while(True):
        display(RandonWord,Guessed, Tries)
        UserInput = input("Adivinar..:").lower()
        while (len(UserInput) > 1 or UserInput.isdigit()):
            print("---Debe ingresar un solo caracter que no sea númerico---")
            UserInput = input("Adivinar..:").lower()
        
        if (not FoundChar(RandonWord,Guessed, UserInput)):
            Tries += 1
        elif gano(RandonWord,Guessed):
            display(RandonWord,Guessed, Tries)
            print("USTED GANO")
            break
   
        if (Tries >= 7):
            display(RandonWord,Guessed, Tries)
            print("USTED PERDIO")
            print("La palabra oculta era: {}".format(RandonWord.upper())) 
            break


if __name__ == '__main__':
    print('B I E N V E N I D O S... (x) Salir')
    game()