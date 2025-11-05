class Weapon:
    total_weapons = 0
    def __init__(self, name:str, ammo:int):
        self.name = name
        self.ammo = ammo
        Weapon.total_weapons += 1

class Soldier:
    def __init__(self, name:str, rank:str, weapon:Weapon):
        self.name = name
        self.rank = rank
        self.weapon = weapon
    def report(self):
        print(f"name: {self.name}, rank:{self.rank}, weapon name: {self.weapon.name}, weapon ammo: {self.weapon.ammo}")
        
class StrikeOption:
    def __init__(self, name:str, ammo:int):
        self.name = name
        self.ammo = ammo
    def strike(self):
        pass
class Tank(StrikeOption):
    def strike(self):
        print("Tank shoots shells.")
class Drone(StrikeOption):
    def strike(self):
        print("A drone can fly.")

class Unit:        
    def __init__(self, unit_name:str, commander:Soldier, strikeoption: StrikeOption, attack):
        self.soldiers = []
        self.unit_name = unit_name
        self.commander = commander
        self.strikeoption = strikeoption
        self.attack = attack
    def briefing(self):
        print(f"unit name: {self.unit_name}, commander: {self.commander.report()}")
        
class Army:
    total_attacks = 0
    def __init__(self, units:list[Unit]):
        self.units = units
    def attack_all(self):
        pass
