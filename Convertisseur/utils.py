from frabriquegrandeur import *

def affcher_error(message):

    print(f"Erreur: {message}")


grandeurs = {
                
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


def show_grandeur():
      
    
        for key in grandeurs.keys():
                
                print(key, end=' ')    
        print()
    

def afficher_resultat(valeur: (int | float), unite_ini: str,resul_conversi: (int | float), vers_unite: str):

        print()
        print(f"la conversion de {unite_ini} vers {vers_unite}")
        print()

        print(f"{valeur} {unite_ini} = {resul_conversi:.4f} {vers_unite}")

        print()


