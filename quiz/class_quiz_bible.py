class Question:
    
    def __init__(self, question: str, propositions: list, repose: int):
        
        
        self.__question = question
        
        self.__porpositions = propositions
        
        self.__reponse = repose
        
    def _get_question(self):
        
        return self.__question
    
    
    def _set_question(self, new):
        
        if isinstance(new, str):
            
            self.__question = new
            
            return self.__question
        
        raise Exception("value is not str")
    
    def _get_proposition(self):
        
        return self.__porpositions
    
    
    def _set_propositions(self,new):        
        
        
        if isinstance(new, list):
            
            self.__porpositions = new
            
            return self.__porpositions
        
        raise Exception("Value is not list")
    
    def _get_reponse(self):
        
        return self.__reponse
    
    def _set_reponse(self, new):
        
        if isinstance(new, int):
            
            self.__reponse = new
            
            return self.__reponse
        
        raise Exception("Value is not str")
    
    question = property(_get_question, _set_question)
    
    propositions = property(_get_proposition, _set_propositions)
    
    reponse = property(_get_reponse, _set_reponse)
    
    








