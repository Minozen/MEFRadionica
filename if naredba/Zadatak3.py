# Prvo pocinjemo tako sto trazimo dva inputa od korisnika; 

jedinica = str(input('Unesi jedinicu (C ili F, velika slova);')) # Prvi je string koji nam kaze koju jedinicu konvertujemo
temp = float(input('Unesi temperaturu;')) # Drugi je float koji sam sluzi kao broj stepena

# Pretvaramo u drugu jedinicu tako sto proveravamo unos stringa "jedinica" i koristimo odgovarajucu formulu

if jedinica == "C":
    print("To je", (temp * 1.8) + 32, "C")
elif jedinica == "F":
    print("To je", (temp - 32) * 5/9, "C") 