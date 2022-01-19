
# Ovde nam se vraca nas stari drug, funkcija! 
def pravougaonik(n, m) :
     
    for i in range(1, n+1) : # Pravimo dva broja-a, i i j koji su za sada nepoznati
        for j in range(1, m+1) :
            if (i == 1 or i == n or # Ovde proveravamo da li je broj koji je unosen jednak sa drugim, jednak sa jedan i ako *jeste* onda stampamo "*" da ne bude prazno kao sto bi generalno bilo ako su brojevi dovoljno mali
                j == 1 or j == m) :
                print("*", end="")           
            else : # A ako *nisu*, onda nastavljamo normalno sa praznim poljem, ovde isto moze da se stavi zvezdica umesto razmaka da se dobije pun pravougaonik
                print(" ", end="")           
         
        print()
 
 
# Ovde trazimo od korisnika visinu i duzinu i koristimo taj integer sa funkcijom "pravougaonik" da napokon dobijemo pravougaonik
visina = int(input('Ukucajte visinu pravougaonika:'))
duzina = int(input('Ukucajte duzinu pravougaonika:'))
pravougaonik(visina, duzina)
 