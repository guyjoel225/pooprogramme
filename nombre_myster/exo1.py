
class Calculatrice:
    
    def __init__(self):
        
        self.nombre1 = float()
        
        
        self.nombre2 = float()
        
    def __add__(self):
        
        return self.nombre1 + self.nombre2
    
    
    def __mult__(self):
        
        
        return self.nombre1 * self.nombre2
    
    
    def __sous__(self):
        
        return self.nombre1 - self.nombre2
    
    
    def __div__(self):
        
        if self.nombre2 != 0:
            return self.nombre1 / self.nombre2

        raise ZeroDivisionError("Error Division par Zero")


    
def afficher(err):
    
    print(f'{err}')
    
    exit(1)
    
    
def main():

    calculatrice = Calculatrice()
    try: 
        
        print()
        
        calculatrice.nombre1 = int(input("Entrez un premier nombre: "))

        print()
        calculatrice.nombre2 = int(input("Entrez un deuxième nombre: "))

        print()
        operateur = input("Entrez un operateur parmie les (+, -, *, /): ")
        
        print()
        
    except Exception as err:
        
        afficher(err)
        
    if operateur == "+":
        
        try:
            
            print(f"{calculatrice.nombre1} + {calculatrice.nombre2} = {calculatrice.__add__()}")
            
            print()
            
        except Exception as err:
            
            afficher(err)
            
    elif operateur == "-":
        
        try:
            
            print(f"{calculatrice.nombre1} - {calculatrice.nombre2} = {calculatrice.__sous__()}")
            
            print()
        
        except Exception as err:
            
            afficher(err)
            
    elif operateur == "*":
        
        try:
            
            print(f"{calculatrice.nombre1} * {calculatrice.nombre2} = {calculatrice.__mult__()}")
            print()

        except Exception as err:
            
            afficher(err)
            
    elif operateur == "/":
        
        try:
            
            print(f"{calculatrice.nombre1} / {calculatrice.nombre2} = {calculatrice.__div__()}")
            print()

        except Exception as err:
            
            afficher(err)
            
    else:
        print("aucun operateur {0} n'existe".format(operateur))
        print()
        
continuer = True     
        

if __name__ == "__main__":
    
    while continuer:
        
    
        main()
        
        print()
        
        quitter = input("Quitter le programme(oui /non ): ").lower()
        
        if quitter == "oui":
            
            continuer = False
            
        else:
            continuer = True
            