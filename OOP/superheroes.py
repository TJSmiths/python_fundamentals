from heroclass import Superhero

batman = Superhero("Batman", "Bruce Wayne", "Unlimited Wealth", "A long list of people")
spiderman = Superhero("Spiderman", "Peter Parker", "Web-Slinging", "Green Goblin")
hulk = Superhero("The Incredible Hulk", "Bruce Banner", "Green Machine", "Thaddeus Ross")
starlord = Superhero("Star-Lord", "Peter Quill", "Total Badass", "Ego")

print(f"Hi, my name is {batman.identity}, although you probably know me as {batman.name}. My superpower is {batman.power} and my arch-nemesis is {batman.arch_enemy}.")
print(f"Hi, my name is {spiderman.identity}, although you probably know me as {spiderman.name}. My superpower is {spiderman.power} and my arch-nemesis is {spiderman.arch_enemy}.")
print(f"Hi, my name is {hulk.identity}, although you probably know me as {hulk.name}. My superpower is {hulk.power} and my arch-nemesis is {hulk.arch_enemy}.")
print(f"Hi, my name is {starlord.identity}, although you probably know me as {starlord.name}. My superpower is {starlord.power} and my arch-nemesis is {starlord.arch_enemy}.")