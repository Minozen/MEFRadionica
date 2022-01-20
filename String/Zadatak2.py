
# Koristimo naseg starog druga funkciju
def vadisamogovornik(text):

 slova = []

 samogovornici = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U',]

 for samogovornik in text:
    if samogovornik in samogovornici:
        slova.append(samogovornik)

 return slova

tekst = str(input("Ukucajte tekst;"))

print("Samogovrnici u tekstu su;", vadisamogovornik(tekst))