class DictionnaireOrdonne:

        def __init__(self, base={}, **donnes):
            
                
                self.cles = []
                
                self.valeurs = []
                
                
                if type(base) not in (dict, DictionnaireOrdonne):
                    
                    raise TypeError("Erreur de type")
                
                
                for cle in base:
                    
                    self[cle] =  base[cle]

                for cle in donnes:
                    
                    self[cle] = donnes[cle]
                    
        
        def __repr__(self):
              
            chaine = "{"
              
            premier_passage = True
              
            for cle, valeur in self.items():
                  
                if not premier_passage:
                      
                    chaine = ", "
                      
                else :
                    premier_passage = False
                    chaine += repr ( cle ) + " : " + repr ( valeur )
                    chaine += " } "
                    
                return chaine
            
        def __str__(self):

                return repr(self)
            
            
        def __len__ ( self ) :
        
            return len ( self.cles )
        
        def __contains__ ( self , cle ) :
        
            return cle in self.cles
        
        
        def __getitem__ ( self , cle ) :

            if cle not in self.cles :
            
                raise KeyError ( "La cl é { 0 } ne se trouve pas dans le dictionnaire " . format (cle ) )

            else :
                    
                    indice = self.cles . index ( cle )
        
            
            return self.valeurs [ indice ]


        def __setitem__ ( self , cle , valeur ) :

                if cle in self.cles :
                    
                    indice = self.cles . index ( cle )
                
                    self.valeurs [ indice ] = valeur
                
                else :
                    
                    self.cles.append ( cle )
                    self.valeurs.append ( valeur )
        
        
        def __delitem__ ( self , cle ) :

            if cle not in self.cles :
                
                raise KeyError (" La cl é { 0 } ne se trouve pas dans le dictionnaire " . format (cle ) )
            
            else :
                    indice = self.cles . index ( cle )
                        
                    del self.cles [ indice ]
                    
                    del self.valeurs [ indice ]
                    
        def __iter__ ( self ) :

                return iter ( self.cles )
            
            
        def __add__ ( self , autre_objet ) :

                if type ( autre_objet ) is not type ( self ) :
                    
                    raise TypeError (" Impossible de concat é ner { 0 } et { 1 } " . format (type ( self ) , type ( autre_objet ) ) )
                
                else :

                    nouveau = DictionnaireOrdonne ()

                
                for cle , valeur in self.items () :
                    
                    nouveau [ cle ] = valeur

                
                for cle , valeur in autre_objet.items () :
                    
                    nouveau [ cle ] = valeur
                
                return nouveau
            
            
        def items ( self ) :

                for i , cle in enumerate ( self.cles ) :
                
                    valeur = self.valeurs [ i ]
                    
                    yield ( cle , valeur )
                    
                    
        def keys ( self ) :

            return list ( self.cles )
        
        def values ( self ) :

                return list ( self . _valeurs )
        
        def reverse ( self ):


            clees = []
            valeures = []
            for cle , valeur in self . items () :

                clees.insert (0 , cle )
                valeures.insert (0 , valeur )

            self.cles = clees
            self.valeurs = valeures
            
            
        def sort ( self ) :

            cles_triees = sorted ( self.cles )

            valeures = []

            for cle in cles_triees :
                
                valeur = self [ cle ]
                valeures.append ( valeur )

            valeures
            self.cles = cles_triees
            self.valeurs = valeures
            
            
            
fruit = DictionnaireOrdonne()


print(fruit)