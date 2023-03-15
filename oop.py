class cat():
    name:None
    age:None
    ishappy:None

    def display(self):
        print("CAT")
        print("name", self.name)
        print("age",self.age)
        print("ishappy",self.ishappy)
    def sound(self):
        print("Meow")
cat1=cat()
cat.name="jack;"
cat.age=6
cat.ishappy=True

cat1.display()
cat1.sound()    