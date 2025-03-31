from converter import *


def grandeur_fabrique(grandeur: str, valeur: (int| float), unite: str):

        converters = {
                
                "longeueur":LongConverter,
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

        if grandeur not in converters:
                
                raise ValueError("Cette grandeur n'est pas prise en charge par ce programme")
        
        return converters[grandeur](valeur,unite)

