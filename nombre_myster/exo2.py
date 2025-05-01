class Grandeur:
    
    types = ["masse","longueur","volume","surface"]
    
    masses  = {"kg":1000,"hg":100,"dag":10,"g":1,"dg":0.1,"cg":0.01,"mg":0.001}
    
    longueurs  = {"km":1000,"hm":100,"dam":10,"m":1,"dm":0.1,"cm":0.01,"mm":0.001}
    
    volumes = {"km3":1000000000,"hm3":1000000,"dam3":1000,"m3":1,"dm3":0.001,"cm3":0.000001,"mm3":0.000000001}
    
    surfaces = {"km2":1000000,"hm2":10000,"dam2":100,"m2":1,"dm2":0.01,"cm2":0.0001,"mm2":0.000001}
    
    
    def __init__(self, la_grandeur, unite, vers_unite, valeur):
    
        self.la_grandeur =  la_grandeur
        
        self.unite = unite
        
        self.vers_unite = vers_unite
        
        self.valeur = valeur
        
        self.grandeur = {"masse":Grandeur.masses, "longueur":Grandeur.longueurs, "volume":Grandeur.volumes, "surface":Grandeur.surfaces}
         
    
    
    
    def menu(self):
        
        for i in self.types:
            
           print(i)
    
    def show_grandeur(self):
        
       
            
        if self.la_grandeur in Grandeur.types:
           
           for key, value in enumerate(self.grandeur):
               
                
            print(self.la_grandeur)
        
        else:
            
            raise Exception("Not grandeur name ", self.la_grandeur)
           
grandeur = Grandeur("volume","km","m",10)


grandeur.menu()

grandeur.show_grandeur()