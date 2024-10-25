import random
"""
En este juego, habrá dos jugadores: el 1er jugador será el usuario y el 2do jugador será la computadora.
"""

def jugar():
    #Creo una variable que guardará la respuesta del usuario.
    usuario = input("Elije una opción: 'pi' para piedra, 'pa' para papel, o 'ti' para tijera.\n").lower() 

    #Variable para la selección escogida por la computadora.
    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        return 'Empate!'

    if gano_el_jugador(usuario, computadora):
        return 'Ganaste!'

    return 'Perdiste!'   

def gano_el_jugador(jugador, oponente): #Función de ayuda
    if ((jugador == 'pi' and oponente == 'ti')
        or(jugador == 'ti' and oponente == 'pa')
        or(jugador == 'pa' and oponente == 'pi')):
        return True

    else:
        return False

print(jugar())            

  

