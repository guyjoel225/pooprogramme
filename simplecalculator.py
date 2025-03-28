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


      


calculatrice1 = Calculator(-8,-10,-16,6)

print(calculatrice1.add())

print(calculatrice1.sous())

print(calculatrice1.mutl())

print(calculatrice1.div())

print(calculatrice1.mod())