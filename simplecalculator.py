#ce projet constera à mettre en palce une calculatrice qui effectue les 4 opération de base:


class Calculator:

      def __init__(self,*args: int):
            
            self.nombres = args


      def add(self,):
            
            return sum(self.nombres)          
      
      def sous(self):
            
            som = self.nombres[0]
            
            for nbre in self.nombres[1:]:

                  som = som - nbre

            return som
      
      def mutl(self):

            prod = self.nombres[0]

            for nbre in self.nombres[1:]:
                  
                  prod = prod * nbre
            return prod
      

      def div(self):

            div = self.nombres[0]

            for nbre in self.nombres[1:]:

                  div = div / nbre

            return div
      
      def mod(self):

            mod = self.nombres[0]

            for nbre in self.nombres[1:]:

                  mod = mod % nbre
            return mod
      


def menu():

      print()

      print("Calculatrice".upper().center(100))

      print()

      print("1. pour effectuer une opération")
      print()
      print("2. pour quitter la calculatrice")
      print()

def oper_sus(valeur:(int | float)) -> (int | float):


                  poursuivre = ""

                  while poursuivre != "=":       

                              print()

                              opeateur = input("precisez l'operateur: (+,-,*,/,%): ")
                              if opeateur == "":
                                     break
                              print()

                              isnotevalue = True

                              while isnotevalue:
                                    
                                    nombre = input("Entrez un nombre: ")

                                    try:
                                          
                                          nombre = int(nombre)

                                    except ValueError:

                                          print("Erreur de conversion")

                                          isnotevalue = True

                                          continue
                                    isnotevalue = False
                              
                              

                              calculat = Calculator(valeur, nombre)

                              if opeateur == "+":
                                    
                                    value = valeur

                                    valeur = calculat.add()

                                    print()

                                    print(f"{value} + {nombre} = {valeur}")

                                    print()

                                    oper_sus(valeur)
                              
                              elif opeateur == "-":

                                    value = valeur

                                    valeur = calculat.sous()

                                    print()

                                    print(f"{value} - {nombre} = {valeur}")

                                    print()
                                    
                                    oper_sus(valeur)
                              elif opeateur == "*":

                                    value = valeur

                                    valeur = calculat.mutl()

                                    print()

                                    print(f"{value} * {nombre} = {valeur}")

                                    print()
                                    
                                    oper_sus(valeur)

                              elif opeateur == "/":

                                    try:
                                          value = valeur

                                          valeur = calculat.div()

                                          print()

                                          print(f"{value} / {nombre} = {valeur}")

                                          print()
                                          
                                          oper_sus(valeur)

                                    except ZeroDivisionError:

                                          print("Zero Division Error")
                                          continue

                        
                              
                              elif opeateur == "%":

                                    try:
                                          value = valeur

                                          valeur = calculat.mod()

                                          print()

                                          print(f"{value} % {nombre} = {valeur}")

                                          print()
                                          
                                          oper_sus(valeur)

                                    except ZeroDivisionError:

                                          print("Zero Division Error")

                                          continue

                              print()
                                    
                              print("cliquez sur enter pour continuer\n")
                              poursuivre = input("entrez égale (=) pour afficher le resultart et quitter ou (q) pour quitter: ")
                              
                              print()

                              if poursuivre == "=":
                                          
                                    print()

                                    print("le resultat = ", valeur)

                                    print()
                                    
                              elif poursuivre.upper() == "Q":
                                    break



continuer = True

while continuer:

      menu()

      choix = int(input("Entrez ici, votre choix: "))

      if choix == 1:

                  liste_nbre = []

                  print()


                  error = True

                  while error:
                        
                        nbre = input("Entrez un nombre: ")

                        try:
                              nbre = int(nbre)

                        except ValueError:

                              print("erreur de conversion")

                              error = True

                              continue

                        error = False

                  oper_sus(nbre)
      
      elif choix == 2:
             
             print()

             print("Merci d'avoir utilisé notre programme!")

             print()

             break
