#multilevel

class foodChain1:
    def tiger(self):
        print("Tiger eats deer")
class foodChain2(foodChain1):
    def deer(self):
        print("Deer eats grass")
class foodChain3(foodChain2):
    def grass(self):
        print("Grass is the primary food source for animals")

r=foodChain3()
r.tiger()
r.deer()
r.grass()

#multiple

class foodChain1:
    def lion(self):
        print("Lion hunts all wild animals")
class foodChain2:
    def cheetah(self):
        print("Cheetah hunts zebra")
class foodchain3(foodChain1,foodChain2):
    def zebra(self):
        print("Zebra eats grass")

r=foodchain3()
r.lion()
r.cheetah()
r.zebra()



