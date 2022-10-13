class isciler():
    def __init__(self, ad, soyad, nomre, maas):
        self.ad = ad
        self.soyad = soyad
        self.nomre = nomre
        self.maas= maas
    def information(self):
        print(
            """
            ad:{}
            soyad:{}
            nomre:{}
            maas:{}
            
            
            """.format(self.ad, self.soyad, self.nomre, self.maas)

            )
class proqramistler(isciler):
    def __init__(self, ad, soyad, nomre, maas, dil):
        super().__init__(ad, soyad, nomre, maas)
        self.dil= dil

    def information(self):
            print(
                """
               Proqramist informasiyalari
                ad:{}
                soyad:{}
                nomre:{}
                maas:{}
                dil:{}
                

                """.format(self.ad, self.soyad, self.nomre, self.maas, self.dil)

            )
    def yeni_dil(self, dil):
     self.dil.append(dil)
    def maas_artir(self, zam_miq):
      print("Maas artirildi")
      self.maas += zam_miq
class direktorlar(isciler):
    def __init__(self, ad, soyad, nomre, maas, isci_say):
        super().__init__(ad, soyad, nomre, maas)
        self.isci_say = isci_say

    def information(self):
        print(

            """
            Direktor Melumatlari
            ad:{}
            soyad:{}
            nomre:{}
            maas:{}
            isci_sayi:{}

            """.format(self.ad, self.soyad, self.nomre, self.maas, self.isci_say)

        )

    def maas_azalt(self, azalma_miq):
        print("Maas azaldildi")
        self.maas -= azalma_miq
    def isci_artir(self, artim_sayi):
        print("Msul olduqu isci sati artirildi")
        self.isci_say += artim_sayi
class investorlar(isciler):
    def __init__(self, ad , soyad, nomre, maas, investisiya):
        super().__init__(ad, soyad, nomre, maas)
        self.investisiya = investisiya

    def information(self):
        print(
            """
            Investor Melumatlari
            ad:{}
            soyad:{}
            nomre:{}
            maas:{}
            investisiya miqdari:{}

            """.format(self.ad, self.soyad, self.nomre, self.maas, self.investisiya)

        )
    def invs_artim(self, invest_artimi):
        self.investisiya += invest_artimi

isci=isciler("eldar","mahmudov",55516548, 100)
isci.information()
proqramist1 = proqramistler("Sabina", "Ecemova", 475289635, 10000, ["C++", "python" ])
proqramist1.information()
proqramist1.yeni_dil("Html")
proqramist1.maas_artir(10)
proqramist1.information()
direktor1 = direktorlar("Sevda", "Babayeva",123456789, 15000, 10)
direktor1.information()
direktor1.maas_azalt(250)
direktor1.isci_artir(5)
direktor1.information()
investor1 = investorlar("Asif", "Mirzayev", 7777777, 20000, 4000)
investor1.information()
investor1.invs_artim(10000)
investor1.information()




