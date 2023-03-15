class cat():
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
        print("name", self.name)
        print("age",self.age)
        print("ishappy",self.ishappy)
    def sound(self):
        print("Meow")
#this is the same as-
cat1=cat("jack,6,true")
#this down below

# cat.name="jack;"
# cat.age=6
# cat.ishappy=True

cat1.display()
cat1.sound()    