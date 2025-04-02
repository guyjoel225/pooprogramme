from nombre import *

from utils import *

print("\n")

print("___________________________________ si tu est fort.e , alors trouve le nombre mystère___________________________________".upper().center(100))

def main():

    essai = 5

    i = 1

    try:

        print()
        
        pseudo = input("Entrez votre pseudo pour votre utilisaeteur: ")

        print()

    except ValueError as e:
        print()

        print(f"erreur: {e}")

        print()
    
    mister = NombreMystere(pseudo)

    while i <= essai:

        print()

        print(f"il vous reste {essai - i } tantative.s")

        print()
        try:

            print()
            nombr = int(input("Trouvez le nombre mystère compris de (1 à 100): "))

            print()

        except ValueError as e:

                print()

                print(f"erreur: {e}")

                print()

                continue

        score = mister.play(nombr)

        if score != 0:
             
             print()

             print(f"Bravo {pseudo} votre  score est: {score}")

             print()

             break
        
        print("")

        i += 1
    print(f"désolé {pseudo} vous avez perdu la partie votre score est: {score}")

    print()
        


if __name__ == "__main__":

        main()
    

    