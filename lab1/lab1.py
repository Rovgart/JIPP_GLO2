def optymalizuj_kursy(wagi_paczek, max_waga):
    wagi_paczek.sort(reverse=True)
    
    kursy = []
    aktualny_kurs = []
    aktualna_waga = 0

    for paczka in wagi_paczek:
        if paczka > max_waga:
            raise ValueError("Paczka jest zbyt duza")
        if aktualna_waga + paczka <= max_waga:
            aktualny_kurs.append(paczka)
            aktualna_waga += paczka
        else:
            kursy.append(aktualny_kurs)
            aktualny_kurs = [paczka]
            aktualna_waga = paczka
    
    if aktualny_kurs:
        kursy.append(aktualny_kurs)
    
    return len(kursy), kursy


wagi_paczek = [18,30,18]
max_waga = 25

liczba_kursow, podzial_na_kursy = optymalizuj_kursy(wagi_paczek, max_waga)

print(f"Minimalna liczba kursów: {liczba_kursow}")
print("Podział paczek na kursy:")
for i, kurs in enumerate(podzial_na_kursy, 1):
    print(f"Kurs {i}: {kurs} (suma wag: {sum(kurs)})")