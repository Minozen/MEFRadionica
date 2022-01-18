# Prvo pitamo korisnika koliki je bio racun i sacuvamo to kao float variable "racun"
racun = float(input('Unesite iznos racuna:'))

# Isto uradimo za procenat baksis-a
baksispr = float(input('Koliki bi hteli da bude procenat baksis?'))

# Jednostavno uzmemo procenat baksisa, podelimo ga sa 100 i pomnozimo sa iznosom racuna, taj "%.2f" samo kaze Python-u da prikaze samo 2 decimale, da nemamo ogroman broj
baksis = "%.2f" % float(baksispr / 100 * racun)

# Stampamo koliko bi trebalo da korisnik plati u baksis-u
print('Baksis bi trebalo da bude;', baksis,'RSD')