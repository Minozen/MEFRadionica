# Za razliku od proslog zadataka, koristicemo "from random import randint" zato sto necemo raditi sa float, broj bi bio previse velik za demonstraciju
from random import randint

# Pravimo oba variable-a sa kasniju kalkulaciju 
x = randint(1, 50)
y = randint(2, 5)

# Stampamo rezultat
print(x, '*', y, '=', x*y)