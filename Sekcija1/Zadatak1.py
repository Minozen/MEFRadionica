# Prvo pocinjemo tako sto cemo definistati funkciju "trougao" sa argumentom "n" koji znacava broj stranica / visinu trougla navedenom u zadatku
def trougao(n):
    mojalista = [] # Lista nam je trenutno prazna ali to je u redu zato sto koristimo metodu "append" koja je vidjena u liniji 5 da dodamo karakter na kraj te prazne liste
    for i in range(1,n+1): # Ta prva jedinica u intervalu nam pomaze da stavimo prvi karakter u nizu, a zatim ponavljamo koliko god puta je vrednost n (koja je variable)+1 velika
        mojalista.append("*"*i) # Ovde stavljamo karakter koji hocemo da koristimo za nas trougao
    print("\n".join(mojalista)) # Stampamo i onda pravimo novu liniju kroz funkciju "/n"

# Pravimo jos jedan variable "n" koji nam definise koliko ce redova nas trougao imati i onda trazimo od korisnika koliki ce biti integer "n"
n = eval(input('Unesi koliko redova bi hteli da bude trougao;' ))
trougao(n)

# Ove funkcije lista su dostupne *samo* u Python 3.x verzijama
