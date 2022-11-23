from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._kori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return len(self._kori)
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        yhteishinta = 0
        for ostos in self._kori:
            yhteishinta += ostos.hinta()
        return yhteishinta

    def lisaa_tuote(self, lisattava: Tuote):
        ostos = Ostos(lisattava)
        
        self._kori.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        lista = []

        for ostos in self._kori:
            i = 0
            loytyi = False
            while i < len(lista):
                if ostos.tuotteen_nimi() == lista[i].tuotteen_nimi():
                    lista[i].muuta_lukumaaraa(1)
                    loytyi = True
                    break
                i += 1
            if not loytyi:
                lista.append(ostos)      

        return lista
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
