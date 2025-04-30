class Items:
    def __init__(self, item_name, item_weight):
        self.item_name = item_name
        self.item_weight = item_weight

    def __str__(self):
        return f"Der Gegenstand {self.item_name} wiegt {self.item_weight} KG"

class Potion(Items):
    def __init__(self, item_name, item_weight, heal_amount=20):
        super().__init__(item_name, item_weight)
        self.heal_amount = heal_amount

    def use_potion(self):
        print(f"Du hast dich mit einem {self.item_name} um {self.heal_amount} Lebenspunkte geheilt")

    def __str__(self):
        return f"Der Heiltrank {self.item_name} wiegt {self.item_weight} KG und heilt {self.heal_amount} Lebenspunkte"

class Weapon(Items):
    def __init__(self, item_name, item_weight, weapon_damage):
        super().__init__(item_name, item_weight)
        self.weapon_damage = weapon_damage

    def attack(self):
        print(f"Du greifst mit der Waffe {self.item_name} und verursachst {self.weapon_damage} Schaden")

    def __str__(self):
        return f"Die Waffe {self.item_name} wiegt {self.item_weight} KG und macht {self.weapon_damage} Schaden"



obj_genericitem = Items("Generischer Gegenstand", 10)
obj_potion = Potion("Starker Heiltrank", 2, 50)
obj_weapon = Weapon("Knüppel", 5, 10)
print(obj_genericitem)
print(obj_potion)
print(obj_weapon)

obj_potion.use_potion()
obj_weapon.attack()
obj_weapon.use_potion()