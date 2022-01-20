# Pocinjemo tako sto cemo traziti unos broja od korisnika i sacuvati ga kao variable "cm"

cm = float(input("Ukucaj duzinu u cm:"))

# Ovde *moramo* da koristimo float a ne integer zato sto delimo sa decimalom, a ne celim brojem

inch = cm/2.54 # Pravimo jos jedan variable koji je je taj float unosen od strane korisnika podeljeno sa 2.54 da dobijemo formulu za ince

if cm <= 0: # Proveravamo da li je broj jednak ili manji nuli
   print("Ubacili ste negativan broj ili nulu, to je neispravna vrednost.")
else:
    print("Duzina u incima:", inch,"in") # Kalkulisemo i stampamo vrednost


