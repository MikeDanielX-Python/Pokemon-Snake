import os
import random

import readchar

# CONSTANTS
POS_X = 0
POS_Y = 1
NUM_TRAINERS = 4
TRAINERS = [[22, 8], [20, 2], [9, 10], [15, 15]]
TRAINER_1 = [22, 8]
TRAINER_2 = [20, 2]
TRAINER_3 = [9, 10]
TRAINER_4 = [15, 15]

VIDA_INICIAL_PIKACHU = 100
VIDA_INICIAL_CHARMANDER = 98
VIDA_INICIAL_SQUIRTLE = 89
VIDA_INICIAL_VENONAT = 80
VIDA_INICIAL_ZUBAT = 79
TAM_BARRA_VIDA = 20

# VARIABLES
my_position = [15, 9]
end_game = False
died = None
vida_actual_pikachu = VIDA_INICIAL_PIKACHU
vida_actual_charmander = VIDA_INICIAL_CHARMANDER
vida_actual_squirtle = VIDA_INICIAL_SQUIRTLE
vida_actual_venonat = VIDA_INICIAL_VENONAT
vida_actual_zubat = VIDA_INICIAL_ZUBAT

# MAP
obstacle_definition = """\
##############################
###########                  #
##############               #
##################           #
#####################        #
###################         ##
###################       ####
##############           #####
#######                 ######
####                  ########
#######                    ###
###########                 ##
################             #
#####################       ##
##################         ###
###############         ######
###########           ########
#####               ##########
##############################\
"""

# Create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

while len(TRAINERS) > 0:
    os.system("cls")
    if end_game:
        break

    # Draw map
    print("+" + ("-" * MAP_WIDTH * 2) + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "
            coach_in_myself = None

            for trainer in TRAINERS:
                if trainer[POS_X] == coordinate_x and trainer[POS_Y] == coordinate_y:
                    char_to_draw = " *"
                    coach_in_myself = trainer

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @"
                if coach_in_myself:
                    TRAINERS.remove(coach_in_myself)
                    print("\n")
                    print("Has encontrado a un entrenador pokemon, preparate para combatir")
                    input("Enter para continuar...")
                    os.system("cls")  # TRAINERS = [[22, 8], [20, 2], [9, 10], [15, 15]]

                    # Define witch trainer you have found
                    name = None
                    first_attack = None
                    second_attack = None
                    vida_actual_enemigo = None
                    VIDA_INICIAL_ENEMIGO = 0
                    DANO_PRIMER_ATAQUE = None
                    DANO_SEGUNDO_ATAQUE = None

                    if my_position[POS_X] == TRAINER_1[POS_X] and my_position[POS_Y] == TRAINER_1[POS_Y]:
                        name = "Charmander"
                        first_attack = "Lanza llamas"
                        second_attack = "Nitro carga"
                        vida_actual_enemigo = vida_actual_charmander
                        VIDA_INICIAL_ENEMIGO = vida_actual_charmander
                        DANO_PRIMER_ATAQUE = 10
                        DANO_SEGUNDO_ATAQUE = 13

                    elif my_position[POS_X] == TRAINER_2[POS_X] and my_position[POS_Y] == TRAINER_2[POS_Y]:
                        name = "Squirtle"
                        first_attack = "Burbuja"
                        second_attack = "Ataque rapido"
                        vida_actual_enemigo = vida_actual_squirtle
                        VIDA_INICIAL_ENEMIGO = vida_actual_squirtle
                        DANO_PRIMER_ATAQUE = 14
                        DANO_SEGUNDO_ATAQUE = 12

                    elif my_position[POS_X] == TRAINER_3[POS_X] and my_position[POS_Y] == TRAINER_3[POS_Y]:
                        name = "Venonat"
                        first_attack = "Chupavidas"
                        second_attack = "Psicorayo"
                        vida_actual_enemigo = vida_actual_venonat
                        VIDA_INICIAL_ENEMIGO = vida_actual_venonat
                        DANO_PRIMER_ATAQUE = 10
                        DANO_SEGUNDO_ATAQUE = 11

                    elif my_position[POS_X] == TRAINER_4[POS_X] and my_position[POS_Y] == TRAINER_4[POS_Y]:
                        name = "Zubat"
                        first_attack = "Mordisco"
                        second_attack = "Bomba lodo"
                        vida_actual_enemigo = vida_actual_zubat
                        VIDA_INICIAL_ENEMIGO = vida_actual_zubat
                        DANO_PRIMER_ATAQUE = 12
                        DANO_SEGUNDO_ATAQUE = 13

                    # Combat
                    while vida_actual_pikachu > 0 and vida_actual_enemigo > 0:
                        # Turno del enemigo
                        print("Turno de {}".format(name))
                        ataque_enemigo = random.randint(1, 2)
                        if ataque_enemigo == 1:
                            print("{} ataca con {}".format(name, first_attack))
                            vida_actual_pikachu -= DANO_PRIMER_ATAQUE
                        else:
                            print("{} ataca con {}".format(name, second_attack))
                            vida_actual_pikachu -= DANO_SEGUNDO_ATAQUE

                        # Vida pokemons
                        if vida_actual_pikachu < 0:
                            vida_actual_pikachu = 0
                        if vida_actual_enemigo < 0:
                            vida_actual_enemigo = 0

                        barra_pikachu = int(vida_actual_pikachu * TAM_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
                        print("Pikachu:    [{}{}][{}/{}]".format("#" * barra_pikachu,
                                                                 " " * (TAM_BARRA_VIDA - barra_pikachu),
                                                                 vida_actual_pikachu, VIDA_INICIAL_PIKACHU))

                        barra_enemigo = int(vida_actual_enemigo * TAM_BARRA_VIDA / VIDA_INICIAL_ENEMIGO)
                        print("{}:    [{}{}][{}/{}]".format(name, "#" * barra_enemigo,
                                                            " " * (TAM_BARRA_VIDA - barra_enemigo),
                                                            vida_actual_enemigo, VIDA_INICIAL_ENEMIGO))

                        input("Enter para continuar...")
                        os.system("cls")

                        # Turno pikachu
                        print("Turno de pikachu")

                        ataque_pikachu = None
                        primer_ataque_pikachu = 21
                        segundo_ataque_pikachu = 24

                        while ataque_pikachu not in ["V", "T"]:
                            ataque_pikachu = input("Elige tu ataque: [Bola [V]oltio, Onda [T]rueno]")

                        if ataque_pikachu == "V":
                            print("Pikachu ataca con Bola Voltio")
                            vida_actual_enemigo -= primer_ataque_pikachu
                        elif ataque_pikachu == "T":
                            print("Pikachu ataca con Onda Trueno")
                            vida_actual_enemigo -= segundo_ataque_pikachu

                        if vida_actual_pikachu < 0:
                            vida_actual_pikachu = 0
                        if vida_actual_enemigo < 0:
                            vida_actual_enemigo = 0

                        barra_pikachu = int(vida_actual_pikachu * TAM_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
                        print("Pikachu:    [{}{}][{}/{}]".format("#" * barra_pikachu,
                                                                 " " * (TAM_BARRA_VIDA - barra_pikachu),
                                                                 vida_actual_pikachu, VIDA_INICIAL_PIKACHU))

                        barra_enemigo = int(vida_actual_enemigo * TAM_BARRA_VIDA / VIDA_INICIAL_ENEMIGO)
                        print("{}:    [{}{}][{}/{}]".format(name, "#" * barra_enemigo,
                                                            " " * (TAM_BARRA_VIDA - barra_enemigo),
                                                            vida_actual_enemigo, VIDA_INICIAL_ENEMIGO))

                        input("Enter para continuar...")
                        os.system("cls")

                    if vida_actual_pikachu > vida_actual_enemigo:
                        print("Pikachu gana")
                        print("Se te ha regenerado la vida")
                        vida_actual_pikachu = VIDA_INICIAL_PIKACHU
                        input("Enter para continuar...")
                        os.system("cls")
                    elif vida_actual_enemigo > vida_actual_pikachu:
                        print("{} gana, has perdido".format(name))
                        end_game = True
                        died = True

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + ("-" * MAP_WIDTH * 2) + "+")

    # Movement
    direction = readchar.readchar()
    new_position = None

    if direction == "w":
        new_position = my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "e":  # <-- Exit
        print("Has salido del juego")
        end_game = True

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position

if died:
    print("\nHas muerto!")
else:
    os.system("cls")
    print("\nFelicidades, derrotaste a todos los pokemon, has ganado!")