#Blackjack

import random

#Función de la baraja de cartas

def crear_baraja():

    figuras=['Corazones','Picas','Diamantes','Trébol']

    valores_cartas=['2','3','4','5','6','7','9','10','J','Q','K','A']

    baraja=[{'valor':valor_carta,'figura':figura}for valor_carta in valores_cartas for figura in figuras]

    random.shuffle(baraja)

    return baraja

#Función para calcular el valor total de una mano

def calcular_valor_mano(mano):

    valor_mano=0

    As_en_mano=False

    for carta in mano:

        if carta['valor'] in ['J','Q','K']:

            valor_mano+=10

        elif carta['valor']=='A':

            As_en_mano=True

            valor_mano=valor_mano+11

        else:

            valor_mano+=int(carta['valor'])

    #Ajustar el valor del As
    
    if As_en_mano and valor_mano>21:

        valor_mano-=10

    return valor_mano

#Función para el reparto de cartas

def reparto_de_cartas(mano):
    
    for carta in mano:

        print(f"{carta['valor']} de {carta['figura']}")

#Función de juego

def comenzar_juego():
    
    baraja=crear_baraja()
    
    mano_jugador=[baraja.pop(),baraja.pop()]

    mano_dealer=[baraja.pop(),baraja.pop()]


    print ("Mano del jugador: ")

    reparto_de_cartas(mano_jugador)

    print("\nMano del dealer: ")

    print(f"Carta oculta")

    print(f"{mano_dealer[1]['valor']} de {mano_dealer[1]['figura']}")
    
    valor_mano_jugador=calcular_valor_mano(mano_jugador)

    print (valor_mano_jugador)

    while valor_mano_jugador<21:

        elección=input("\n¿Quieres otra carta o te plantas? (c/p)").lower()

        if elección=='c':

            mano_jugador.append(baraja.pop())

            print("\nMano del jugador: ")

            reparto_de_cartas(mano_jugador)

            valor_mano_jugador=calcular_valor_mano(mano_jugador)

        elif elección=='p':

            break

    if valor_mano_jugador>21:

        print("\n¡Te has pasado! ¡Gana el dealer!")

    else:

        print(("\nMano del dealer:"))

        reparto_de_cartas(mano_dealer)

        valor_mano_dealer=calcular_valor_mano(mano_dealer)


        while valor_mano_dealer<17:

            mano_dealer.append(baraja.pop())

            valor_mano_dealer=calcular_valor_mano(mano_dealer)

        print("\nMano del dealer: ")

        reparto_de_cartas(mano_dealer)

        if valor_mano_dealer>21:

            print("\n¡El dealer se ha pasado!¡Has ganado!")

        elif valor_mano_dealer>valor_mano_jugador:

            print("\n¡Ha ganado el dealer!")

        elif valor_mano_dealer<valor_mano_jugador:

            print("\n¡Has ganado!")

        else:

            print("\n¡Es un empate!")
    
# Empezar el juego

comenzar_juego()













    
