class Cat():
    name:None
    age:None
    ishappy:None

    # constructor
    def __init__(self, name,age,ishappy ):
        self.name=name
        self.age=age
        self.ishappy=ishappy


    def display(self):
        print("CAT")
        print("name:", self.name)
        print("age:",self.age)
        print("is happy?",self.ishappy)

    def sound(self):
        print("Meow!")

# Child Class
class DomesticCat(Cat):

    owner:None
    
    def display(self):
        print("Domestic ")
        super().display()
        print("owner:",self.owner)

    def __init__(self, owner,name, age, ishappy):
        super().__init__(name,age,ishappy)
        self.owner=owner

class WildCat(Cat):

    def hunt(self):
        print("i am hunting...")
    def sound(self):
        print("Meooowwwwww...")


#this is the same as-
Cat1=DomesticCat("Jane","jack",6,True)
#this down below
#cat.owner="Jane"
# cat.name="jack;"
# cat.age=6
# cat.ishappy=True

Cat1.display()
Cat1.sound()    

cat2=WildCat("bob",2,False)

cat2.display()
cat2.sound()
cat2.hunt()