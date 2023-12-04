class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edelliset_arvot = []

    def miinus(self, operandi):
        self._tallenna_edellinen()
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._tallenna_edellinen()
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._tallenna_edellinen()
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._tallenna_edellinen()
        self._arvo = arvo
    
    def kumoa(self):
        if len(self._edelliset_arvot) > 0:
            self._arvo = self._edelliset_arvot.pop()

    def arvo(self):
        return self._arvo

    def _tallenna_edellinen(self):
        self._edelliset_arvot.append(self._arvo)
