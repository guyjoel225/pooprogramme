from converter import *



def grandeur_fabrique(grandeur: str, valeur: (int| float), unite: str):

        grandeur_factor = {
                
                "longueur":LongConverter,
                "poids":PoidMasseConverter,
                "masse":PoidMasseConverter,
                "temperature":TempsConverter,
                "aire":AireConverter,
                "volume":VolumeConverter,
                "temps":TempsConverter,
                "vitesse":VirtessConverter,
                "energie":EnergieConverter,
                "pression":PressionConverter,
                "surface":SurfaceConverter,
                "data":DataConverter

        }

        if grandeur not in grandeur_factor:
                
                raise ValueError("Cette grandeur n'est pas prise en charge par ce programme")
        print("la grandeur existe")
        return grandeur_factor[grandeur](valeur,unite)
