import random 

import string

class PasswdGenrator:

        minuscules = string.ascii_lowercase
        
        majuscules = string.ascii_uppercase

        digits =  "0123456789"

        caract_speciaux = string.punctuation


        def __init__(self, length: int, digite: bool, majuscule: bool, minuscule: bool, ponct:  bool):
                
                self.length = length
                self.digite =  digite
                self.majuscule = majuscule
                self.minuscule = minuscule
                self.ponct = ponct


        
        def generateur(self):
                
                caracteres = ""

                if self.digite:
                        
                        caracteres += self.digits
                
                if self.majuscule:
                        
                        caracteres += self.majuscules

                if self.minuscule:
                        
                        caracteres += self.minuscules

                if self.ponct:
                        
                        caracteres += self.caract_speciaux

                if not caracteres:
                        raise ValueError("Aucun caractère choisi")
                
                password  =  ''.join(random.choice(caracteres) for _ in range(self.length))


                return password
        
