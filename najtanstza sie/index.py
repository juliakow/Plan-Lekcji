class Zbiory:
    def __init__(self, n):
        self.rodzic = list(range(n))
        self.ranga = [0] * n

    def znajdz(self, miasto):
        if self.rodzic[miasto] != miasto:
            self.rodzic[miasto] = self.znajdz(self.rodzic[miasto])
        return self.rodzic[miasto]

    def polacz(self, miasto1, miasto2):
        korzen1 = self.znajdz(miasto1)
        korzen2 = self.znajdz(miasto2)
        if korzen1 != korzen2:
            if self.ranga[korzen1] > self.ranga[korzen2]:
                self.rodzic[korzen2] = korzen1
            elif self.ranga[korzen1] < self.ranga[korzen2]:
                self.rodzic[korzen1] = korzen2
            else:
                self.rodzic[korzen2] = korzen1
                self.ranga[korzen1] += 1

def kruskal(n, krawedzie):
    zbiory = Zbiory(n)
    drzewo = []
    calkowity_koszt = 0

    krawedzie.sort(key=lambda x: x[2])

    for u, v, koszt, energia in krawedzie:
        if zbiory.znajdz(u) != zbiory.znajdz(v):
            zbiory.polacz(u, v)
            drzewo.append((u, v))
            calkowity_koszt += koszt * energia

    return drzewo, calkowity_koszt

def wczytaj_dane():
    linie_odleglosci = [
        "A B 5",
        "A C 3",
        "B C 2",
        "B D 1",
        "C D 3",
        "D E 2",
        "A D 10",
        "F G 1",
        "F H 3",
        "G H 2",
        "D H 1"
    ]

    linie_energii = [
        "A 10",
        "B 5",
        "C -5",
        "D -10",
        "E -5",
        "F 10",
        "G -5",
        "H -5"
    ]

    indeksy_miast = {}
    obecny_indeks = 0
    krawedzie = []
    bilans_energii = []

    for linia in linie_energii:
        miasto, energia = linia.split()
        if miasto not in indeksy_miast:
            indeksy_miast[miasto] = obecny_indeks
            obecny_indeks += 1
        bilans_energii.append((indeksy_miast[miasto], int(energia)))

    for linia in linie_odleglosci:
        miasto1, miasto2, odleglosc = linia.split()
        if miasto1 not in indeksy_miast:
            indeksy_miast[miasto1] = obecny_indeks
            obecny_indeks += 1
        if miasto2 not in indeksy_miast:
            indeksy_miast[miasto2] = obecny_indeks
            obecny_indeks += 1
        u = indeksy_miast[miasto1]
        v = indeksy_miast[miasto2]
        odleglosc = int(odleglosc)
        energia = sum([eb[1] for eb in bilans_energii if eb[0] == u or eb[0] == v])
        krawedzie.append((u, v, odleglosc, energia))

    return obecny_indeks, krawedzie, bilans_energii

def glowna():
    n, krawedzie, bilans_energii = wczytaj_dane()
    drzewo, calkowity_koszt = kruskal(n, krawedzie)
    print("Minimalne drzewo rozpinajace (polaczenia miedzy miastami):")
    for u, v in drzewo:
        print(f"{u} - {v}")
    print(f"Calkowity koszt budowy sieci energetycznej: {calkowity_koszt}")

if __name__ == "__main__":
    glowna()