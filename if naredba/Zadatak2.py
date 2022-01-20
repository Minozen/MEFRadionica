# Posto naravno ne mozemo ocekivati korisnika da pogodi "1.458432754267", koristicu integer umesto float

# Prvo stavljamo potrebne dodatke
from random import randint

slucajanbr = randint(1,10)

korisnikbr = int(input('Pogodi broj;')) # Licno mi se nije svidelo to sto ste uputili na "eval", generalno je sto bolja praksa da se eval izbegava

if slucajanbr == korisnikbr:
    print('Bravo, to je taj broj!')
else:
    print('Uf, probaj opet. Moj broj je bio', slucajanbr)

# Kao beleska, hteo bi samo da kazem da je ovaj zadatak vec bio uradjen u vasem fajlu iz radionice