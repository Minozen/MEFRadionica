import numpy as np
from sympy import zeros

# Pocinjemo sa 3 inputa gde trazimo tri broja od korisnika i cuvamo ih kao x, y i z


# Mogli bi da napravimo funkciju "prosek_br" koju cu ostaviti kao komentar
def prosek_br(x, y, z):
    pr = (x + y + z)/3
    return pr

x = eval(input('Unesite prvi broj;'))
y = eval(input('Unesite drugi broj;'))
z = eval(input('Unesite treći broj;'))

# Ovde zovemo funkciju
prosek = prosek_br(x, y, z)

# Ovo je najjednostavniji nacin, samo uzmemo proizvod ta 3 broja i podelimo ga sa 3 da dobijemo prosek
#prosek = (x + y + z)/3

print(prosek)

