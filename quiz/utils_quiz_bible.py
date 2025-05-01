import random

from class_quiz_bible import Question

class Niveau:
    
    def __init__(self):
        
        self.__niveau = list()
        
        self.__score = 0
        
        self.__conteur = 0
        
        self.__continuer = len(self.__niveau)
        
        
    def _get_niveau(self):
            
        return self.__niveau
    
    
    def _set_niveau(self, new):
        
        if isinstance(new, list):
            
            self.__niveau = new
            
            return self.__niveau
        
        raise Exception("Value is not list")
    
    
    niveau = property(_get_niveau, _set_niveau)
    
    
    def melanger(self):
        
        
        random.shuffle(self.niveau)
        
        

    
    def start(self):
        
        self.melanger()
        
        
        print()
        
        print("______________________________________quiz biblique___________________________________".upper().center(100))
        
        print()
        
        
        while  self.__conteur <= self.__continuer:
            
            
            for question in self.niveau:
                
                self.__conteur += 1
                
                print()
                
                print(f"{self.__conteur}. {question.question}")
                
                print()
                
                for answer in question.propositions:
                    
                    print(answer)
                    
                print()
               
                try:
                    
                    repondre = int(input("Entrez votre proposition de réponse: "))
                    
                    print()    
                    
                    if repondre == question.reponse:
                        
                        self.__score += 1
                        
                        print("Bravo! très bien joué ............score:{}".format(self.__score))
                        
                    else:
                            print("Oups!, perdu! .................. score: {}".format(self.__score))
                            
                except Exception as err:
                    
                    print()
                    print(err)
                    
                    self.stop()
                        
                    
        
        return self.__score
    
    
    
    def stop(self):
        
        exit(1)  
    
    
#NIVEAU FACILE


questionf1 = Question("Qui a créé le ciel et la terre? ",["1. L'homme", "2. Satan", "3. DIEU"], 3)

questionf2 = Question("Quel fruit a-t-elle mangé dans le jadin d'Éden? ",["1. Pomme", "2. Fruit de l'abre de la connaissance du bien et ru mal", "3. Raisin"], 2)

questionf3 = Question("Combien de jours Dieu a-t-il pris pour créer le monde? ",["1. 3 jours", "2. 6 jours", "3. 7 jours"], 2)

questionf4 = Question("Quel homme a construit une arche pour échapper au déluge? ",["1. Abraham", "2. Moïse", "3. Noé"], 3)

questionf5 = Question("Qui fut vendu par ses frères en Égypte? ",["1. Joseph", "2. David", "3. Esaü"], 1)

questionf6 = Question("Comment s'appelait la mer que Moïse a traversée avec les Israélites?",["1. Mer Noire", "2. Mer Morte", "3. Mer Rouge"], 3)

questionf7 = Question("Qui a réçu les 10 commandements?",["1. Moïse", "2. Aaron", "3. Élie"], 1)

questionf8 = Question("Quel roi d'Israel a tué Goliath?",["1. Saül", "2. Salomon", "3. David"], 3)

questionf9 = Question("Quelle femme est devenue reine en Peste et a sauvé les Juifs?",["1. Ruth", "2. Esther", "3. Marie"], 2)

questionf10 = Question("Quel prophète a été avalé par un grand poisson?",["1. Jonas", "2. Jérémie", "3. Ésaïe"],1)

questionf11 = Question("Combien de disciples JÉSUS avait-il?",["1. 10", "2. 12", "3. 14"], 2)

questionf12 = Question("Qui a trahi JÉSUS?",["1. Pierre", "2. Jean", "3. Judas"], 3)

questionf13 = Question("Où JÉSUS est-il né?",["1. Jérusalem", "2. Nazareth", "3. Bethléem"], 3)

questionf14 = Question("Quel est le premier livre de la Bible?",["1. Génèse", "2. Exode", "3. Psaumes"], 1)

questionf15 = Question("Quel est le dernier le livre de la Bible?",["1. Apocalypse", "2. Actes", "3. Hébreux"], 1)


niveau_facile = [questionf1, questionf2, questionf3, questionf4, questionf5, questionf6, questionf7, questionf8, questionf9, questionf10,
                 questionf11, questionf12, questionf13, questionf14, questionf15]






#NIVEAU MOYEN



questionm1 = Question("Quel patriarche est le père d'Isaac?", ["1. Jacob", "2. Abraham", "3. Moïse"], 2)

questionm2 = Question("Quel était le signe de l'alliance entre DIEU et Noé?", ["1. L'étoile", "2. L'arc-en-ciel", "3. La colombe"], 2)

questionm3 = Question("Combien de plaies DIEU a-t-il envoyées sur l'Égypte?", ["1. 7", "2. 10", "3. 12"], 2)

questionm4 = Question("Quelle est la première femme mentionnée dans la Bible?", ["1. Sara", "2. Ève", "3. Rébecca"], 2)

questionm5 = Question("Comment s'appelle le frère d'Aaron?", ["1. Moïse", "2. Josué", "3. Samuel"], 1)

questionm6 = Question("Qui est resté trois jours dans le ventre du grand poisson?", ["1. Daniel", "2. Jonas", "3. Paul"], 2)

questionm7 = Question("Quel roi a écrit la majorité des psaumes?", ["1. Salomon", "2. David", "3. Ézéchias"], 2)

questionm8 = Question("Comment s'appelle la femme de Boaz?", ["1. Esther", "2. Marie", "3. Ruth"], 3)

questionm9 = Question("Combien de temps les Israélites ont-ils érré dans le désert?", ["1. 40 jours", "2. 70 ans", "3. 40 ans"], 3)

questionm10 = Question("Qui a reçu la vision des ossements desséchés?", ["1. Ésaïe", "2. Ézechiel", "3. Jérémie"], 2)

questionm11 = Question("Dans quelle ville JÉSUS a-t-il transformé l'eau en vin?", ["1. Capernaüm", "2. Jérusalem", "3. Cana"], 3)

questionm12 = Question("Qui a nié JÉSUS trois fois?", ["1. Judas", "2. Pierre", "3. Thomas"], 2)

questionm13 = Question("Quel apotre est connu pour avoir douté de la resurrection de JÉSUS?", ["1. Paul", "2. Jean", "3. Thomas"], 3)

questionm14 = Question("Qui a écrit le livre de l'Apocalypse?", ["1. Jean", "2. Pierre", "3. Jacques"], 1)

questionm15 = Question("Quelle femme fut la prémière à voir JÉSUS?", ["1. Marie de Béthanie", "2. Marie-Madeleine", "3. Marthe"], 2)




niveau_moyen = [questionm1, questionm2, questionm3, questionm4, questionm5, questionm6, questionm7, questionm8, questionm9, questionm10, questionm11,
                questionm12, questionm13, questionm14, questionm15]


#NIVEAU DIFICILE

questiond1 = Question("Qui fut le roi d’Israël pendant la construction du premier temple à Jérusalem ?",["1. David", "2. Salomon", "3. Roboam"],2)

questiond2 = Question("Quel prophète a vu une échelle atteignant le ciel dans un rêve ?",["1. Jacob", "2. Joseph", "3. Samuel"],1)

questiond3 = Question("Combien de chapitres compte le livre d'Ésaïe ?",["1. 66", "2. 72", "3. 50"],1)

questiond4 = Question("Qui a été frappé de cécité sur le chemin de Damas ?",["1. Paul", "2. Pierre", "3. Barnabas"],1)

questiond5 = Question("Quelle femme juge a dirigé Israël ?",  ["1. Déborah", "2. Abigaïl", "3. Ana"], 1)

questiond6 = Question("Dans quel livre trouve-t-on l’histoire de la tour de Babel ?", ["1. Genèse", "2. Exode", "3. Juges"], 1)

questiond7 = Question("Quel roi a vu la main écrire sur le mur pendant un festin ?",  ["1. Nebucadnetsar", "2. Belschatsar", "3. Darius"], 2)

questiond8 = Question("Combien de fois les enfants d’Israël ont-ils tourné autour de Jéricho avant que les murs tombent ?", ["1. 7 fois", "2. 6 fois", "3. 13 fois"], 3)

questiond9 = Question("Combien de livres contient le Nouveau Testament ?", ["1. 27", "2. 39", "3. 66"], 1)

questiond10 = Question("Quelle était la profession de Luc, l’auteur de l’Évangile selon Luc ?",  ["1. Pêcheur", "2. Médecin", "3. Collecteur d'impôts"], 2)

questiond11 = Question("Quel est le seul livre de la Bible qui ne mentionne pas le nom de Dieu ?", ["1. Esther", "2. Ruth", "3. Cantique des cantiques"], 1)

questiond12 = Question("Quel est le plus long psaume ?", ["1. Psaume 23", "2. Psaume 119", "3. Psaume 90"],2)

questiond13 = Question("Combien de jours Jésus est-il resté sur terre après sa résurrection ?", ["1. 3 jours", "2. 40 jours", "3. 50 jours"], 2)

questiond14 = Question("Quel apôtre a écrit l’épitre aux Hébreux selon la tradition (bien que l’auteur ne soit pas nommé) ?",  ["1. Paul", "2. Pierre", "3. Jacques"], 1)

questiond15 = Question("Comment s'appelle l'ange qui a annoncé la naissance de Jean-Baptiste et de Jésus ?", ["1. Michel", "2. Raphaël", "3. Gabriel"], 3)


niveau_dificile =  [questiond1, questiond2, questiond3, questiond4, questiond5,questiond6, questiond7, questiond8, questiond9,
                    questiond10, questiond11, questiond12, questiond13, questiond14,questiond15]



