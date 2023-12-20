from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class Peli:
    def __init__(self) -> None:
        self.kps_pelaaja_vs_pelaaja = KPSPelaajaVsPelaaja()
        self.kps_tekoaly = KPSTekoaly()
        self.kps_parempi_tekoaly = KPSParempiTekoaly()

    def pelaaja_vs_pelaaja(self):
        print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
        self.kps_pelaaja_vs_pelaaja.pelaa()
    
    def tekoaly(self):
        print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
        self.kps_tekoaly.pelaa()

    def parempi_tekoaly(self):
        print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
        self.kps_parempi_tekoaly.pelaa()