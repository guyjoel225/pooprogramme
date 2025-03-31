class Converter:

    def __init__(self,valeur: (int | float), unite: str):

            self.valeur = valeur

            self.unite = unite

    
    def converters(self, vers_unit):

            raise NotImplementedError("Methode à implémenter dans les sous-classes")
    
    def show(self):
           
           raise NotImplementedError("Methode à implémenter dans les sous -classes")
    

#la classe de la grandeur  Longueur

class LongConverter(Converter):
       
       # l'unité est le mètre (m)
        longueur_factors = {
                
                "km":1000,
                "hm":100,
                "dam":10,
                "m":1,
                "dm":0.1,
                "cm":0.01,
                "mm":0.001,
                "mile":1609.34,
                "yard":0.9144,
                "pied":0.3048,
                "pouce":0.0254,
                "Mile marin":1852
        }


        def converters(self, vers_unit: str):
                
                if vers_unit not in self.longueur_factors:
                        
                        raise ValueError("cette unité n'est pas prise en charge pour ce programme.")
                based_valeur = self.valeur * self.longueur_factors[self.unite]

                conversion = based_valeur / self.longueur_factors[vers_unit]

                return conversion

        def show(self):
               
               return list(self.longueur_factors.keys())




#la classe de la grandeur  poids/masse

class PoidMasseConverter(Converter):
       
       # unité le kilogramme (kg)

        poidmasseconverter_factors = {
                "t":1000,
                "kg":1,
                "hg":0.1,
                "dag":0.01,
                "g":0.001,
                "dg":0.0001,
                "cg":0.00001,
                "mg":0.000001,
                "livre":0.453592,
                "once":0.0283495,
                "carat":0.0002,
                "grain":0.00006479891
        }


        def converters(self, vers_unite: str):
               
                if vers_unite not in self.poidmasseconverter_factors:
                        
                        raise ValueError("Cette unité n'est pas prise en compte dans ce programme!")
                
                base_value = self.valeur * self.poidmasseconverter_factors[self.unite]


                conversion = base_value / self.poidmasseconverter_factors[vers_unite]

                return conversion
        
        def show(self):
               
               return list(self.poidmasseconverter_factors.keys())
        


#la classes de grandeur temperature

class Temperature(Converter):
       
        temperature_factors = ["celsius","fahrenheit","kelvin"]

        def converters(self,vers_unit: str):
                
                if vers_unit not in self.temperature_factors:
                        
                        raise ValueError("cette unité n'est pas prise en charge dans ce programme")
                
                if self.unite == vers_unit:
                        
                        return self.valeur
                
                if self.unite == "celsius" and vers_unit == "fahrenheit":
                        
                        conversion = (self.valeur * 9/5) + 32

                        return conversion

                elif self.unite =="fahrenheit" and vers_unit == "celsius":
                        
                        conversion == (self.valeur - 32) * 5/9

                        return conversion
                
                elif self.unite =="celsius" and vers_unit == "kelvin":
                        
                        conversion = self.valeur + 273.15

                        return conversion
                
                elif self.unite == "kelvin" and vers_unit == "celsius":
                        
                        conversion = self.valeur - 273.15

                        return conversion
                
                elif self.unite == "fahrenheit" and vers_unit == "kelvin":
                        
                        conversion = (self.valeur -32) * 5/9 + 273.15

                        return conversion
                
                elif self.unite == "kelvin" and vers_unit == "fahrenheit":
                        
                        conversion = (self.valeur - 273.15) * 9/5 + 32

                        return conversion
                
        

        def show(self):
                
                return self.temperature_factors




#classe de la grandeur aire


class AireConverter(Converter):
        
        #unité le metre carré

        aire_factors = {
                "km2":1000000,
                "hm2":10000,
                "ha":10000,
                "aire":100,
                "m2":1,
                "pied2":0.092903,
                "yard2":0.836127,
                "acre":4046.86,
                "dam2":100,
                "dm2":0.01,
                "cm2":0.0001,
                "mm2":0.000001
        }


        def converters(self, vers_unit):
                
                if vers_unit not in self.aire_factors:
                        
                        raise ValueError("Cette unité n'est pas prise en charge dans programme.")
                
                base_valeur = self.valeur * self.aire_factors[self.unite]

                conversion  = base_valeur / self.aire_factors[vers_unit]

                return conversion
        

        def show(self):
                
                return list(self.aire_factors.keys())
        


#classe de la grandeur volume


class VolumeConverter(Converter):
        
        pass



#classe de la grandeur temps


class TempsConverter(Converter):
        pass


#classe de la grandeur vitesse


class VirtessConverter(Converter):
        
        pass


#classe de la grandeur energie


class EnergieConverter(Converter):
        
        pass


#classes de la grandeur pression


class PressionConverter(Converter):
        pass


#classe de la grandeur surface

class SurfaceConverter(Converter):
        
        pass

#classe de la grandeur données

class DataConverter(Converter):
        
        pass


