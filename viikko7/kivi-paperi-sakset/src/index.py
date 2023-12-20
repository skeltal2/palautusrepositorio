from peli import Peli


def main():
    peli = Peli()

    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            peli.pelaaja_vs_pelaaja()
        elif vastaus.endswith("b"):
            peli.tekoaly()
        elif vastaus.endswith("c"):
            peli.parempi_tekoaly()
        else:
            break


if __name__ == "__main__":
    main()
