import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote
from pankki import Pankki
from kirjanpito import Kirjanpito

class TestKauppa(unittest.TestCase):
    def setUp(self) -> None:
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 2)
            if tuote_id == 3:
                return Tuote(3, "liha", 10)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
    
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5)
    
    def test_kahden_eri_tuotteen_ostoksen_paatyttya_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 7)
    
    def test_kahden_saman_tuotteen_ostoksen_paatyttya_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 10)
    
    def test_kaksi_tuotetta_toinen_loppu_ostoksen_paatyttya_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5)
    
    def test_aloita_asiointi_nollaa_edellisen_ostoksen(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 2)
    
    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "1111")

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "1111")


        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

        self.kauppa.aloita_asiointi
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "1111")


        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 3)
    
    def test_poista_korista(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 0)
    
    def test_kirjanpitoa_kutsutaan(self):
        kirjanpito = Kirjanpito()
        pankki = Pankki(kirjanpito)
        
        pankki.tilisiirto(None, None, None, None, None)

        self.assertEqual(len(kirjanpito.tapahtumat), 1)
    
    def test_tuotteet_yhtasuuria(self):
        maito_1 = self.varasto_mock.hae_tuote(1)
        maito_2 = self.varasto_mock.hae_tuote(1)

        self.assertTrue(maito_1 == maito_2)
    
    def test_tuote_str(self):
        maito = self.varasto_mock.hae_tuote(1)

        self.assertTrue(str(maito) == "maito")
    
    def test_varasto_hae(self):
        varasto = Varasto()
        tuote = varasto.hae_tuote(1)

        self.assertTrue(tuote == Tuote(1, "", 0))
    
    def test_varasto_hae_olemassaoleton_tuote(self):
        varasto = Varasto()
        tuote = varasto.hae_tuote(99)

        self.assertIsNone(tuote)

    def test_varasto_saldo(self):
        varasto = Varasto()
        saldo = varasto.saldo(1)

        self.assertEqual(saldo, 100)

    def test_ota_varastosta(self):
        varasto = Varasto()
        tuote = varasto.hae_tuote(1)
        varasto.ota_varastosta(tuote)
        saldo = varasto.saldo(1)

        self.assertEqual(saldo, 99)
    
    def test_palauta_varastoon(self):
        varasto = Varasto()
        tuote = varasto.hae_tuote(1)
        varasto.ota_varastosta(tuote)
        varasto.palauta_varastoon(tuote)
        saldo = varasto.saldo(1)

        self.assertEqual(saldo, 100)
    
    def test_viitegeneraattori_laskee_oikein(self):
        vg = Viitegeneraattori()
        self.assertEqual(vg.uusi(), 2)
        self.assertEqual(vg.uusi(), 3)

