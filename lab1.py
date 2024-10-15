def optymalizuj_kursy(wagi_paczek, max_waga):
    # Sortujemy paczki malejąco
    wagi_paczek.sort(reverse=True)
    
    kursy = []
    aktualny_kurs = []
    aktualna_waga = 0

    for paczka in wagi_paczek:
        if aktualna_waga + paczka <= max_waga:
            aktualny_kurs.append(paczka)
            aktualna_waga += paczka
        else:
            kursy.append(aktualny_kurs)
            aktualny_kurs = [paczka]
            aktualna_waga = paczka
    
    # Dodajemy ostatni kurs, jeśli nie jest pusty
    if aktualny_kurs:
        kursy.append(aktualny_kurs)
    
    return len(kursy), kursy

# Przykładowe użycie
wagi_paczek = [10, 5, 8, 3, 7, 2, 4, 6]
max_waga = 15

liczba_kursow, podzial_na_kursy = optymalizuj_kursy(wagi_paczek, max_waga)

print(f"Minimalna liczba kursów: {liczba_kursow}")
print("Podział paczek na kursy:")
for i, kurs in enumerate(podzial_na_kursy, 1):
    print(f"Kurs {i}: {kurs} (suma wag: {sum(kurs)})")