class Dog:
    def __init__(self, name:str, age:int):
        self.name = name                    
        self.age = age

    def sit(self):
        print(f"O {self.name} sentou")

    def roll_over(self):
        print(f"O {self.name} rolou")

meu_cahorro = Dog("Jurandir",7)
meu_cahorro.sit()
meu_cahorro.roll_over()                