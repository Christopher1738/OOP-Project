import random
from datetime import datetime

class Pet:
    def __init__(self, name, species="dog"):
        self.name = name
        self.species = species.lower()
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.cleanliness = 8
        self.tricks = []
        self.birthday = datetime.now()
        self.favorite_food = self._assign_favorite_food()
    
    def _assign_favorite_food(self):
        favorites = {
            "dog": "bone",
            "cat": "fish",
            "rabbit": "carrot",
            "bird": "seeds"
        }
        return favorites.get(self.species, "pet food")
    
    def eat(self, food_type=None):
        if food_type == self.favorite_food:
            self.hunger = max(0, self.hunger - 4)
            self.happiness = min(10, self.happiness + 2)
            print(f"{self.name} loves {food_type}! ♥")
        else:
            self.hunger = max(0, self.hunger - 3)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} ate some food.")
    
    def sleep(self):
        hours = random.randint(3, 8)
        self.energy = min(10, self.energy + hours // 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} slept for {hours} hours. Zzz...")
    
    def play(self, game="fetch"):
        if self.energy < 2:
            print(f"{self.name} is too tired to play.")
            return
        
        games = {
            "fetch": (2, 3, 1),
            "chase": (3, 2, 2),
            "hide and seek": (1, 4, 1)
        }
        
        energy_cost, happiness_gain, hunger_gain = games.get(game, (2, 2, 1))
        
        self.energy -= energy_cost
        self.happiness = min(10, self.happiness + happiness_gain)
        self.hunger = min(10, self.hunger + hunger_gain)
        print(f"{self.name} played {game} and had fun!")
    
    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Species: {self.species.capitalize()}")
        print(f"Age: {(datetime.now() - self.birthday).days} days")
        
        stats = {
            "Hunger": self.hunger,
            "Energy": self.energy,
            "Happiness": self.happiness,
            "Cleanliness": self.cleanliness
        }
        
        for name, value in stats.items():
            print(f"{name}: {'★' * value}{'☆' * (10 - value)} {value}/10")
    
    def train(self, trick):
        if random.random() > 0.3:  # 70% success chance
            self.tricks.append(trick)
            print(f"🎉 {self.name} learned '{trick}'!")
        else:
            print(f"😅 {self.name} didn't learn it this time.")
    
    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} knows no tricks yet.")
        else:
            print(f"{self.name}'s tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")