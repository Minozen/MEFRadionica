# Prvo pocinjemo tako sto cemo uneti dodatak random
# Zasto nismo samo uradili "from random import randint"? Zato sto funkcija "randint" radi samo sa *integer*, a ne sa float, koristim float zato sto nam daje vecu varijaciju u broju nego da smo koristili samo cele brojeve (integer)
import random


brojevi=[]

# Pravimo variable "br1" koji se sastoji od slucajnih float-a od 1 do 50

for n in range(1, 51): # Pravimo for petlju koja generise pseudo-slucajni broj (float) 50 puta i stavlja ga u listu "brojevi"
    br = random.uniform(3,6)
    brojevi.append(br)

# Onda stampamo tekst naveden u print statement-u i stampamo listu "brojevi"

print('Slucajani brojevi izmedju 3 i 6;', brojevi)