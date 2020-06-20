# class Çalışan():

#     # def __init__(self):
#     #     self.kabiliyetleri = []
#     #     self.unvanı = 'işçi'
#     #     self.maaşı = 1500
#     #     self.memleketi = ''
#     #     self.doğum_tarihi = ''

#     def __init__(self, a,b,c,d,e):
#         self.kabiliyetleri = a
#         self.unvanı = b
#         self.maaşı = c
#         self.memleketi = d
#         self.doğum_tarihi = e




# # ali = Çalışan()
# # ali.kabiliyetleri.append("Hızlı")
# # ali.kabiliyetleri.append("Çalışkan")
# # ali.unvanı = "Yönetici"
# # ali.maaşı = 1000

# # veli = Çalışan()
# # veli.kabiliyetleri.append("Test")
# # veli.unvanı = "Yardımcı"
# # veli.maaşı = 2000

# # ahmet = Çalışan()
# # ahmet.maaşı = 3000

# ali = Çalışan(["Hızlı", "Çalışkan"],"Yönetici",1000)
# veli = Çalışan(["Test"],"Yardımcı", 2000)
# ahmet = Çalışan([], "İşçi", 3000)


# print("Ali kabiliyetleri = %s, unvanı=%s, maaşı=%s"%(ali.kabiliyetleri,ali.unvanı,ali.maaşı))
# print("Veli kabiliyetleri = %s, unvanı=%s, maaşı=%s"%(veli.kabiliyetleri,veli.unvanı,veli.maaşı))
# print("Ahmet kabiliyetleri = %s, unvanı=%s, maaşı=%s"%(ahmet.kabiliyetleri,ahmet.unvanı,ahmet.maaşı))






# ------------------------------------------------------------------------

"""
- İki oyuncu olsun
- Oyuncunun ismi, aldığı darbe, canı, enerjisi olacak
- bu iki oyuncu birbirine şu iki müdahaleyi yapabilecek
    1: Saldırı
    2: Kaçmak
- Saldırı olduğunda random olarak 0,1,2 rakamlarından biri seçilir
    0 olduğunda herhangi bir taraf zarar görmez
    1 olduğunda saldıran taraf darbe vurur
    2 olduğunda saldıran taraf darbe yer
- Her darbede 1 enerji azalır
- Her 5 enerji azalımında 1 can gider
- can sıfır olan oyuncu kaybeder
"""


import time
import random
import sys


# class Oyuncu:

#     def __init__(self, isim, can, enerji):
#         self.isim = isim
#         self.can = can
#         self.enerji = enerji
#         self.darbe = 0


#     def saldir(self,rakip):

#         sonuc = random.randint(0,2)

#         if sonuc==0:
#             print("Berabere")
#         elif sonuc==1:
#             print("Siz darbe vurdunuz")
#             self.darbe_vur(rakip)
#         elif sonuc==2:
#             print("Siz darbe yediniz")
#             self.darbe_vur(self)

#         self.sonuca_bak(rakip)


#     def darbe_vur(self,oyuncu):
#         oyuncu.darbe += 1
#         oyuncu.enerji -= 1

#         if oyuncu.enerji%5==0:
#             oyuncu.can -= 1

#     def sonuca_bak(self,rakip):
#         kazanan = None
#         if self.can<1:
#             kazanan = rakip.isim

#         if rakip.can<1:
#             kazanan = self.isim

#         if kazanan==None:
#             print("Sizin durumunuz = can=%s enerji=%s darbe=%s" %(self.can,self.enerji,self.darbe))
#             print("Rakibin durumu  = can=%s enerji=%s darbe=%s" %(rakip.can,rakip.enerji,rakip.darbe))
#         else:
#             print("Kazanan Oyuncu = {}".format(kazanan))




# birinci_oyuncu  = Oyuncu("Serkan",1,5)
# ikinci_oyuncu   = Oyuncu("Halil Polat",1,5)

# while True:
#     hamle = input("İslemi Giriniz (s,c) : ")
#     if hamle=="s":
#         birinci_oyuncu.saldir(ikinci_oyuncu)
#     elif hamle=="c":
#         break






class Oyuncu:

    def __init__(self, isim, can, enerji):
        self.isim = isim
        self.can = can
        self.enerji = enerji
        self.darbe = 0


    def darbe_al(self):
        self.darbe += 1
        self.enerji -= 1
        if self.enerji%3==0:
            self.can -= 1




class Oyun:

    def __init__(self, birinci_oyuncu, ikinci_oyuncu):
        self.birinci_oyuncu = birinci_oyuncu
        self.ikinci_oyuncu = ikinci_oyuncu
        self.hamle_sayisi = 0

    def baslat(self):
        while True:
            hamle = self.hamle_sor()
            if hamle=="s":
                bitti_mi = self.saldir(birinci_oyuncu,ikinci_oyuncu)

                if bitti_mi:
                    break
            elif hamle=="c":
                break

    def saldir(self, saldiran, savunan):
        sonuc = random.randint(0,30)

        if sonuc>0 and sonuc<10:
            print("beraber")
        elif sonuc>=10 and sonuc<=20:
            self.ikinci_oyuncu.darbe_al()
            print("Darbe alan = %s" % ikinci_oyuncu.isim)
        elif sonuc>20 and sonuc<=30:
            self.birinci_oyuncu.darbe_al()
            print("Darbe alan = %s" % birinci_oyuncu.isim)

        self.hamle_sayisi += 1
        return self.sonuca_bak()

    def sonuca_bak(self):
        kazanan = None

        if self.birinci_oyuncu.can==0:
            kazanan = self.ikinci_oyuncu
        elif self.ikinci_oyuncu.can==0:
            kazanan = self.birinci_oyuncu

        if kazanan==None:
            print("Birinci Oyuncu = can=%s enerji=%s darbe=%s" %(self.birinci_oyuncu.can,self.birinci_oyuncu.enerji,self.birinci_oyuncu.darbe))
            print("İkinci Oyuncu  = can=%s enerji=%s darbe=%s" %(self.ikinci_oyuncu.can,self.ikinci_oyuncu.enerji,self.ikinci_oyuncu.darbe))
        else:
            print("Kazanan Oyuncu = %s" % kazanan.isim)
            print("Toplam Hamle = %s" % self.hamle_sayisi)

        return True if kazanan!=None else False

    def hamle_sor(self):
        return input("Hamlenizi giriniz : (s:Saldırı c:Cikis) : ")



birinci_oyuncu = Oyuncu("Serkan", 3,9)
ikinci_oyuncu = Oyuncu("Emine", 3, 9)

oyun = Oyun(birinci_oyuncu, ikinci_oyuncu)
oyun.baslat()




