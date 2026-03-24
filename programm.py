def ievade():
    kos = int(input("Kostīmu skaits kuru jāizgatavo: "))
    pog = float(input("pogas cena: "))
    rav = float(input("rāvējslēdzeja cena: "))
    aud = float(input("auduma cena(par metru): "))
    Aprekini(kos, pog, rav, aud)


def Aprekini(kos, pog, rav, aud):
    NepiecAud = kos * 2.5
    NepiecPog = kos*3
    NepiecRav = kos
    KopejIzmaksas = NepiecAud * aud + NepiecPog * pog + NepiecRav * rav
    FaktAud = NepiecAud * 0.88  # 12 procenti ir zaudeti
    izvade(NepiecAud, NepiecPog, NepiecRav, KopejIzmaksas, FaktAud)


def izvade(NepiecAud, NepiecPog, NepiecRav, KopejIzmaksas, FaktAud):
    print(
        f"Nepieciešams: {NepiecAud} metri auduma,{NepiecPog} pogas,{NepiecRav} rāvējslēdzēju")
    print(f"Kopejas izmaksas: {KopejIzmaksas} eiro")
    print(f"Faktiski izmantoto auduma daudzums pec zudumiem: {FaktAud} metri")


ievade()
