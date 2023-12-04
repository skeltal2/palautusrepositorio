KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            kapasiteetti = KAPASITEETTI
        self.kapasiteetti = kapasiteetti
        self.validoi_parametri(self.kapasiteetti)

        if kasvatuskoko is None:
            kasvatuskoko = OLETUSKASVATUS
        self.kasvatuskoko = kasvatuskoko
        self.validoi_parametri(self.kasvatuskoko)

        self.lukujono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0
    
    def validoi_parametri(self, parametri):
        if not isinstance(parametri, int) or parametri < 0:
            raise Exception("Huono parametri")

    def kuuluu(self, n):
        return n in self.lukujono

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.lukujono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm >= len(self.lukujono):
                vanha_lukujono = self.lukujono
                self.lukujono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(vanha_lukujono, self.lukujono)

            return True

        return False

    def poista(self, n):
        loydetty = False

        for i, luku in enumerate(self.lukujono):
            if i > self.alkioiden_lkm:
                break
            if loydetty:
                self.lukujono[i - 1] = self.lukujono[i]
            if n == luku:
                loydetty = True
                self.lukujono[i] = 0
                self.alkioiden_lkm -= 1

        return loydetty

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def alkioiden_maara(self):
        return self.alkioiden_lkm

    def poista_tyhjat(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        for luku in b.lukujono:
            a.lisaa(luku)
        return a

    @staticmethod
    def leikkaus(a, b):
        x = IntJoukko()
        for luku in a.lukujono:
            if a.kuuluu(luku) and b.kuuluu(luku):
                x.lisaa(luku)
        return x

    @staticmethod
    def erotus(a, b):
        for luku in b.lukujono:
            a.poista(luku)
        return a

    def __str__(self):
        return "{" + ", ".join(map(str, self.poista_tyhjat())) + "}"