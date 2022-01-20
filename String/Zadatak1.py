string = str(input('Unesite tekst;'))

duzina = len(string) # Ovde koristimo funkciju "len" da saznamo duzinu teksta i da vadimo specificne karaktere kad je potrebno
print("Vas tekst ima", len(string), "karaktera.") # Stampamo duzinu
print("Stampamo tekst 10 puta...")
for i in range (1, 11):
    print(string)
print("Prvo slovo u tekstu je;", string[0])
print("Prva tri slova u tekstu su;", string[0:3])
print("Zadnja tri slova u tekstu su;", string[duzina -3:])

if duzina >= 7: # Proveravamo ako string ima 7 ili vise karaktera
    print("Sedmo slovo u tekstu je;", string[6]) # Ako ima, stampamo sedmo slovo
else:
    print("Tekst ima manje od 7 karaktera, stampanje sedmog znaka nije moguce")

print("Vas tekst sa sve velikim slovima;", string.upper())
