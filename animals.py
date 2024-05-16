class Dog:
    hunger_level = 100
    scientific_name = "Canis lupus familiaris"

    def __init__(self, name):
        self.name = name
        self.woofs = 0
        self.is_trained = False

    def feed(self, amount):
        if self.hunger_level >= amount:
            self.hunger_level -= amount
        else:
            self.hunger_level = 0

    def speak(self):
        print(f"{self.name}: Woof!")

    def hear(self, words):
        if self.name.lower() in words.lower():
            self.speak()
            self.is_trained = True

    def count(self):
        self.woofs += 1
        for bark in range(self.woofs):
            self.speak()


class Dalmatian(Dog):

    def __init__(self, name):
        super().__init__(name)

    def count(self):
        self.woofs += 2
        for bark in range(self.woofs):
            self.speak()


class Retriever(Dog):

    def __init__(self, name):
        super().__init__(name)
        self.is_trained = True



