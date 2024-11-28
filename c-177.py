#Private variable code
class SC():
    def __init__(self):
        self.__score= 1
        
    def gscore(self):
        print(self.__score)
        
    def uscore(self):
        self.__score= self.__score +2
        print(self.__score)
        
player= SC()
player.__score=100
player.gscore()
player.uscore()
player.uscore()

#Public Variable Code
class SC():
    def __init__(self):
        self.score= 1
        
    def gscore(self):
        print(self.score)
        
    def uscore(self):
        self.score= self.score +2
        print(self.score)
        
player= SC()
player.score=100
player.gscore()
player.uscore()
player.uscore()
player.uscore()

 
'''Why should a self parameter be passed when creating a __init__() function? 

Whenever a function which is defined inside a class will be called from outside that class using its object. Then that function requires a self parameter as when the function is called using an object the instance(you can imagine it as object name but in computer language) of that object is always passed along with the function as a parameter which gets stored inside the self parameter


'''
