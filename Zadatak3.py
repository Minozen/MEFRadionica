# Najlakse resenje je da sve manuelno pomnozimo 

# Uzimamo broj od korisnika i sacuvamo ga kao "x"
x = eval(input('Unesite broj;'))

# Pravimo 5 variable-a, svaki mnozi broj "x" sa svojim brojem
proizvod1 = (int(x) * 1)
proizvod2 = (int(x) * 2)
proizvod3 = (int(x) * 3)
proizvod4 = (int(x) * 4)
proizvod5 = (int(x) * 5)

# Na kraju stampamo vrednosti svih "proizvod"-a i stavljamo sep od "---"
print(proizvod1, proizvod2, proizvod3, proizvod4, proizvod5, sep = '---')