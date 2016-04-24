#always include "object" in parenthesis when creating a new class
class Musician(object):
    
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)],)
            print('')

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self, sounds):
        # Call the __init__ method of the parent class
        super(Bassist).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician): #The Guitarist class is the child of the Musician class
    def __init__(self, sounds):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
    
class Drummer(Musician):
    def __init__(self, sounds):
        super(Drummer, self).__init__(["Boom", "Ting", "Tap"])
    
    def count_up(self):
        print("One... Two... Three... Four...")
    
    def combust(self):
        print("Kaboom!!!!!")

"""
nigel = Guitarist(Musician)
nigel.solo(6)
print(nigel.sounds)
"""
pete = Drummer(Musician)
pete.solo(3)
pete.count_up()
pete.combust()
