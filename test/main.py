import random

class Person:
    def __init__(self, name, health=0, mood=0, money=0.0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return (f"\n=== {self.name} ===\n"
                f"Здоров'я: {self.health}\n"
                f"Настрій: {self.mood}\n"
                f"Капітал: {self.money}\n")

    def change_state(self, health=0, mood=0, money=0.0):
        if self.health + health < 0:
            print(f"Людина {self.name} померла через критичне здоров'я!")
            return False
        if self.mood + mood < 0:
            print(f"Людина {self.name} впала в депресію!")
            return False
        if self.money + money < 0:
            print(f"Людина {self.name} збанкрутувала!")
            return False

        self.health += health
        self.mood += mood
        self.money += money
        return True

class Action:
    def __init__(self, name, health=0, mood=0, money=0.0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return (f"\n=== Дія: {self.name} ===\n"
                f"Вплив на здоров'я: {self.health}\n"
                f"Вплив на настрій: {self.mood}\n"
                f"Вплив на гроші: {self.money}\n")

people = [
    Person(name="Тарас", health=100, mood=100, money=50),
    Person(name="Іван", health=120, mood=80, money=30),
    Person(name="Олена", health=90, mood=110, money=70)
]

while people:
    for person in people[:]:
        action = Action(
            name="Робота",
            health=random.randint(-10, -5),
            mood=random.randint(-20, -10),
            money=random.randint(50, 100)
        )
        print(action)
        if not person.change_state(
            health=action.health,
            mood=action.mood,
            money=action.money
        ):
            print(f"{person.name} вибув зі списку!\n")
            people.remove(person)
        print(person)

    if not people:
        print("Усі ресурси закінчилися. Гра завершена!")
        break
