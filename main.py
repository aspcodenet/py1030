import data.databas

print(data.databas.a)

class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.phone = ""


p = Person("Stefan", 52)
p.City = "Stockholm"
p.Bla = 12
print(p.name)


def calculateTotalPrice(priceExMoms:int, moms:int) -> int :
    total = priceExMoms + moms
    return total



calculateTotalPrice("3312312","apa")

while True:
    price =  int(input("Ange pris ex moms:"))
    moms = int(input("moms:"))
    total = calculateTotalPrice(price,moms)
    print(f"Totala priset blev {total} kronor")



x = 12
y = 12

for i in range(0,5): # 0,1,2,3,4
    print(i)


myChildren = ["Fanny", "Josefine", "Oliver"]
myChildren.append("Musse")
for barn in myChildren:
    print(barn)



antal = len(myChildren)
print(f"Stefan har {antal} barn")
barn1 = myChildren[i]
    


if x == 12:
    print("Hej") 
    print("Hopp")


namn = "Stefan"
print(namn)
namn = 'Holmberg'
namn = namn.upper()
print(namn)
print(len(namn))
#namn = 12


