from utils_quiz_bible import *

niveau1 = Niveau()

niveau1.niveau = niveau_facile


niveau2 = Niveau()

niveau2.niveau = niveau_moyen

niveau3 = Niveau()


niveau3.niveau = niveau_dificile


def quiz():

        global niveau1, niveau2, niveau3
        
        print()
        print("Niveau: 1")
        
        score1 = niveau1.start()
        
        if score1 >= 10:
            
            print()
            print("Niveau: 2")
            
            score2 = niveau2.start()
            
        if score2 >= 10:
            
            print()
            print("Niveau: 3")
            
            niveau3.start()
            

if __name__ == "__main__":
    
    quiz()
    
    