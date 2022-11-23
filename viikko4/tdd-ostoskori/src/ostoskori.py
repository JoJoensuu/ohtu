from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._kori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        lukumaara = 0
        for ostos in self._kori:
            lukumaara += ostos.lukumaara()

        return lukumaara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        yhteishinta = 0
        for ostos in self._kori:
            yhteishinta += ostos.hinta()
        return yhteishinta

    def lisaa_tuote(self, lisattava: Tuote):
        loytyi = False
        for tuote in self._kori:
            if tuote.tuotteen_nimi() == lisattava.nimi():
                tuote.muuta_lukumaaraa(1)
                loytyi = True
        if not loytyi:
            ostos = Ostos(lisattava)
            self._kori.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        for tuote in self._kori:
            if tuote.tuotteen_nimi() == poistettava.nimi():
                if tuote.lukumaara() > 1:
                    tuote.muuta_lukumaaraa(-1)
                else:
                    self._kori.remove(tuote)
                return

    def tyhjenna(self):
        self._kori = []

    def ostokset(self):
        return self._kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
