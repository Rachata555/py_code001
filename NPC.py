class NPC:
    def __init__(self,s_name,HP,Mana):
        self.name =s_name
        self.HP = HP
        self.Mana = Mana
    def describe(self):
        print(f"name: {self.name}")
        print(f"HP: {self.HP}")
        print(f"Mana: {self.Mana}")
        print("-"*20)
        
    def heal(self,heal):
        self.HP += heal

n1 = NPC("Alice",100,150)
n2 = NPC("Bob",100,250)


n1.heal(20)
n1.describe()

n2.heal(30)
n2.describe()