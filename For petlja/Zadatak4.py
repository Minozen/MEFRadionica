ime = str(input('Unesi svoje ime:'))

# Definisemo funkciju "ponoviime"
def ponoviime(n):
    lista1 = []
    for i in range(1, n+1):
        lista1.append(ime)
    print("\n".join(lista1))

# Pravimo jos jedan variable "n" koji nam definise koliko ce redova nas trougao imati i onda trazimo od korisnika koliki ce biti integer "n"
n = eval(input('Unesi koliko puta bi hteo da ponovis svoje ime;' ))
ponoviime(n)

# Ovaj primer jeste veoma slican (vise skoro identican) ali je super demostrancija kako znanje u jednom polju programiranja u ovakom jeziku visokog-nivoa se lako prenosi u druga polja