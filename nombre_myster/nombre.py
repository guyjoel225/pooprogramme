from random import randrange

from utils import *


class User:

    def __init__(self,pseudo):
        
        self.pseudo = pseudo

        self.score =  0



class NombreMystere(User):

    start = 1
    stop =  100

    nombre_mystere = randrange(start, stop)

    def play(self, nombre: int):



            if  nombre == self.nombre_mystere:

                self.score = 10

                return self.score
            
            elif nombre > self.nombre_mystere:

                print("la valeur est trop grande!")

            if nombre < self.nombre_mystere:

                print("La valeur est trop petite")

            if  nombre + 10 == self.nombre_mystere or nombre - 10 == self.nombre_mystere:

                print("juste à coté")

            if nombre < 1 or nombre > 100:

                print("votre nombre sort de l'intervalles predéfinie")


            return self.score
            


