class Superhero():
    def __init__(self, name, identity, power, arch_enemy):
        self.name = name
        self.identity = identity
        self.power = power
        self.arch_enemy = arch_enemy
    
    def introduce(self):
        print(f"Hi, my name is {self.identity}, although you probably know me as {self.name}. My superpower is {self.power} and my arch-nemesis is {self.arch_enemy}.")