
class Octane():
        def __init__(self, accountName):
                self.accountName = accountName
                self.currentPrice = 0
        
        def discount(self, discount:float):
                self.price = self.price - (self.price * discount)
            
        def no_discount(self):
                self.price = self.price 
        
def get_octanes():
        premium = Octane("Premium 93")
        premium.price = 4.68

        sidegrade = Octane("Midgrade 89")
        sidegrade.price = 4.55

        regular = Octane("Regular 87")
        regular.price = 4.42

        gradeList = [premium, sidegrade, regular]
        return gradeList

def get_octane(gradeList: list):
        pick = -2
        while pick < 0:
                thisVar = 0
                if pick == -1:
                        print("Invalid choice, please try again")
                for acc in gradeList:
                        thisVar += 1
                        print(f"{thisVar}: {acc.accountName}, {acc.price}")
                
                try:
                        pick = int(input("Which level of octane do you wish to use? \n"))
                        if pick < 1 or pick > len(gradeList):
                                pick = -1
                except:
                        pick = -1
                pick -= 1
        return gradeList[pick]
