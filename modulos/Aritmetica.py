class Aritmetica:
    def __init__(self):
        self.__suma  = 0
        self.__resta = 0
        self.__multi = 0
        self.__divi  = 0


    def getSuma(self):
        return self.__suma


    def setSuma(self, valor_1, valor_2):
        self.__suma = float(valor_1) + float(valor_2)


    def getResta(self):
        return self.__resta 


    def setResta(self, valor_1, valor_2):
        self.__resta = float(valor_1) - float(valor_2)
    

    def getMulti(self):
        return self.__multi 


    def setMulti(self, valor_1, valor_2):
        self.__multi = float(valor_1) * float(valor_2)


    def getDivi(self):
        return self.__divi 


    def setDivi(self, valor_1, valor_2):
        self.__divi = float(valor_1) / float(valor_2)


