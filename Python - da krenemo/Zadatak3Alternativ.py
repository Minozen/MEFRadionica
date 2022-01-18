# Najlakse resenje je tako sto cemo dodati numpy za laksu matematiku 
import numpy as np

# Trazimo unos broja od korisnika i sacuvamo ga kao integer "broj"
broj = int(input('Unesite broj;'))

# Ova lista je puna brojeva koje cemo koristiti da mnozimo onaj koji je korisnik ubacio
list2 = [1, 2, 3, 4, 5]

# Koristimo numpy funkciju "multiply" da pomnozimo obe "liste"
rezultat = np.multiply(broj, list2)

# Napokon, spajamo celu listu brojeva preko funkcije "join" i stavljamo "---" da razdvojimo brojeve
razmak = '---'.join(str(v) for v in rezultat)

# Stampamo rezultat
print(razmak)

