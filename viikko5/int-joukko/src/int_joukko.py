KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

        if self.alkioiden_lkm == len(self.ljono):
            self.nosta_kapasiteettia()

    def nosta_kapasiteettia(self):
        kapasiteetin_lisays = [0 for x in range(self.kasvatuskoko)]
        self.ljono += kapasiteetin_lisays

    def poista(self, n):
        if n in self.ljono:
            self.ljono.remove(n)
            self.alkioiden_lkm -= 1
            self.ljono.append(0)
        
    def kopioi_taulukko(self, vanha, uusi):
        for i in range(len(vanha)):
            uusi[i] = vanha[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = []
        for i in range(self.alkioiden_lkm):
            taulu.append(self.ljono[i])
        return taulu

    @staticmethod
    def yhdiste(a, b):
        uusi_joukko = IntJoukko()
        for i in range(a.alkioiden_lkm):
            uusi_joukko.lisaa(a.ljono[i])
        for i in range(b.alkioiden_lkm):
            uusi_joukko.lisaa(b.ljono[i])
        return uusi_joukko

    @staticmethod
    def leikkaus(a, b):
        uusi_joukko = IntJoukko()
        for i in range(a.alkioiden_lkm):
            if b.kuuluu(a.ljono[i]):
                uusi_joukko.lisaa(a.ljono[i])
        return uusi_joukko

    @staticmethod
    def erotus(a, b):
        uusi_joukko = IntJoukko()
        for i in range(a.alkioiden_lkm):
            if a.ljono[i] not in b.ljono:
                uusi_joukko.lisaa(a.ljono[i])
        return uusi_joukko

    def __str__(self):
        tuotos = "{"
        if self.alkioiden_lkm == 1:
            tuotos += str(self.ljono[0])
        elif self.alkioiden_lkm > 1:
            for i in range(self.alkioiden_lkm - 1):
                tuotos += str(self.ljono[i]) + ", "
            tuotos += str(self.ljono[self.alkioiden_lkm - 1])
        tuotos += "}"
        return tuotos
