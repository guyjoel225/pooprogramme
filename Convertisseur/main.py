from frabriquegrandeur import grandeur_fabrique
from utils import *

def main():

    print()

    print("Bienvenue dans le convertisseur de grandeur")

    try:

        print()

        show_grandeur()

        print()

        gdeur = input("Entrez une grandeur: ")

        print()

        val = float(input("Entrez la valeur: "))

        print()

        unit = input("Entrez l'unité de départ: ")

        print()

        convers = grandeur_fabrique(gdeur,val,unit)
        
        unites = convers.show()

        print()

        for unt in unites:

            print(unt , end=" ")
            
        print()

        print("\n")

        vers_unit = input("Entrez l'unité vers laquelle vous comptez convertir: ")

        print()

        result = convers.converters(vers_unit)
        print()

        afficher_resultat(val,unit,result, vers_unit)

        print()
        
    except ValueError as e:

        affcher_error(e)


if __name__ == "__main__":

    main()