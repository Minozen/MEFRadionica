# Imamo dva resenja ovde, prvi je "lak" i taj cu ostaviti kao komentar

#print('*')
#print('**')
#print('***')
#print('****')
#print('*****')

# Kao sto vidimo, ovaj nacin je lenj i ne-elegantan, moje licno resenje bi bilo ovako;

# Pocinjemo tako sto pravimo variable "n" cija vrednost ce biti 5
n = 5

for i in range(1, n+1): # Ovo kaze Python-u da pocnemo od 1, a da zaustavimo kod n+1, sto je 6 (zapamtite da Python broji od 0)
    # Ovo je ta "petlja" koju cemo proci kroz toliko puta kolko je sirok opseg u prosloj liniji (15)
    for k in range(1, i+1):
        print("*", end="") # Stampamo zvezdicu i zavrsavamo tu, onda pocinjemo opet ali sa i+1, zapamtite, *svaki put kad Python prodje kroz petlju, taj "i" se poveca za 1*
    print()