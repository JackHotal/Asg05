class Coffee:
    
    def __init__(self, brand, d, c):
        self.__brand = brand
        self.__d = d
        self.__c = c
        self.__k = 10
        self.__h = c/3
        
    def Q(self):
        q = ((2*self.__d*self.__k)/self.__h)**(.5)
        return q
    
    def TAC(self):
        tac = ((self.Q()/2)*self.__h)+((self.__d*self.__k)/self.Q())+(self.__d*self.__c)
        return tac
    
    def T(self):
        t = (self.Q()/self.__d)*52
        return t
    
    def __str__(self):
        """ Returns the string representation for this object """
        Q = self.Q()
        TAC = self.TAC()
        T = self.T()
        return '{0:<16s}{1:<16,.2f}{2:<16,.2f}{3:<16,.2f}{4:<16,.2f}{5:<16,.2f}'.format(self.__brand,
        self.__c, self.__d, Q, TAC, T)
    
    
    
    
    
    
    def __eq__(self, other):
        """ Defines equality of bank account objects"""
        return self.__account_number == other.__account_number
    
    def __lt__(self, other):
        """ Defines the less than operator for bank account objects """
        return self.__account_number < other.__account_number   
    
