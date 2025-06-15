class NPC:
    def __init__(self,s_name,s_HP,s_Mana):
        self.name =s_name
        self.HP = s_HP
        self.Mana = s_Mana
    def describe(self):
        print(f"name: {self.name}")
        print(f"HP: {self.HP}")
        print(f"Mana: {self.Mana}")
        print("-"*20)

n1 = NPC("Alice",100,150)
n2 = NPC("Bob",100,250)

n1.describe()
n2.describe()