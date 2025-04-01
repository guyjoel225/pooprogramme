from passwdgen import PasswdGenrator

print("\n")

print("_______________________________GENERATEUR DE MOT DE PASSE_______________________________".upper().center(100))

print("")

def main():

    print()

    try: 
        
        length = int(input("Entrez la longueur de votre mot de passe(par defaut la longueur sera 12): ".upper())or 12)


        print()

        digite = input("ajouter les valeurs numérique(y/n): ".upper()).lower() == "y"

        print()

        majuscule = input("Ajouter les lettre majuscule(y/n): ".upper()).lower() == "y"

        print()

        minuscule = input("Ajouter les Minuscule(y/n): ".upper()).lower() == "y"

        print()

        carat_sp = input("Ajouter les caractères spéciaux(y/n): ".upper()).lower() =="y"

        print()

        mot_de_pass = PasswdGenrator(length,digite,majuscule,minuscule,carat_sp)

        pwd = mot_de_pass.generateur()

        print("********************************************************************".center(136))
        print()
        print(f"mot de passe: {pwd}".center(140))
        print()
        print("********************************************************************".center(136))
    except ValueError as e:
            
            print(f"erreur: {e}")



if __name__ == "__main__":
     
        main()