# class Çalışan():
#     personel = []

#     def __init__(self, isim):
#         self.isim = isim
#         self.kabiliyetleri = []
#         self.personele_ekle()

#     @classmethod
#     def personel_sayısını_görüntüle(cls):
#         print(len(cls.personel))

#     def personele_ekle(self):
#         self.personel.append(self.isim)
#         print('{} adlı kişi personele eklendi'.format(self.isim))

#     @classmethod
#     def personeli_görüntüle(cls):
#         print('Personel listesi:')
#         for kişi in cls.personel:
#             print(kişi)

#     def kabiliyet_ekle(self, kabiliyet):
#         self.kabiliyetleri.append(kabiliyet)

#     def kabiliyetleri_görüntüle(self):
#         print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
#         for kabiliyet in self.kabiliyetleri:
#             print(kabiliyet)


# print(dir(Çalışan))

# ahmet = Çalışan('Ahmet')
# mehmet = Çalışan('Mehmet')
# ayşe = Çalışan('Ayşe')

# Çalışan.personel_sayısını_görüntüle()

# class Sınıf():
#     sınıf_niteliği = 0

#     def __init__(self, veri):
#         self.veri = veri

#     def örnek_metodu(self):
#         return self.veri

#     @classmethod
#     def sınıf_metodu(cls):
#         return cls.sınıf_niteliği

#     @staticmethod
#     def statik_metot():
#         print('merhaba statik metot!')

# Sınıf.statik_metot()



# class Sınıf():
#     __gizli = 'gizli'

#     def bana_gizli_ogeyi_ver(self):
#       return self.__gizli

#     def örnek_metodu(self):
#         print(self.__gizli)
#         print('örnek metodu')

#     @classmethod
#     def sınıf_metodu(cls):
#         print('sınıf metodu')

#     @staticmethod
#     def statik_metot():
#         print('statik metot')



# # print(Sınıf.__gizli)
# #print(Sınıf.sınıf_metodu())
# orn = Sınıf()
# print(orn.bana_gizli_ogeyi_ver())




# class Çalışan():
#     _personel = []

#     def __init__(self, isim):
#         self._isim = isim
#         self.personele_ekle()

#     def personele_ekle(self):
#         self._personel.append(self._isim)
#         print('{} adlı kişi personele eklendi'.format(self._isim))

#     @classmethod
#     def personeli_görüntüle(cls):
#         print('Personel listesi:')
#         for kişi in cls._personel:
#             print(kişi)

#     @property
#     def isim(self):
#         return self._isim

#     @isim.setter
#     def isim(self, yeni_isim):
#         kişi = self._personel.index(self.isim)
#         self._personel[kişi] = yeni_isim
#         self._isim = yeni_isim
#         print('yeni isim: ', yeni_isim)


# ahmet = Çalışan("Ahmet")
# mehmet = Çalışan("Mehmet")
# ali = Çalışan("Ali")


# Çalışan.personeli_görüntüle()

# mehmet.isim = "Yeni Mehmet"
# Çalışan.personeli_görüntüle()
# print(mehmet.isim)



# class Program():
#     _version = "0.1"

#     def __init__(self):
#         pass

#     @property
#     def versiyon(self):
#         return self._version

#     @versiyon.setter
#     def versiyon(self,yeni_deger):
#         self._version = yeni_deger



# orn = Program()
# orn.versiyon = "0.2"
# print(orn.versiyon)




class Oyuncu():
    def __init__(self, isim, rütbe):
        self.isim = isim
        self.rütbe = rütbe
        self.güç = 0

    def hareket_et(self):
        print('hareket ediliyor...')

    def puan_kazan(self):
        print('puan kazanıldı')

    def puan_kaybet(self):
        print('puan kaybedildi')



class Asker(Oyuncu):
    memleket = 'Arpaçbahşiş'

    def __init__(self,isim,rütbe):
        super().__init__(isim,rütbe)
        self.güç = 100

    def örnek_metodu(self):
        pass

    def hareket_et(self):
        super().hareket_et()
        print("asker saldırıya geçti")

class İşçi(Oyuncu):
    pass

class Yönetici(Oyuncu):
    pass




asker = Asker("Ahmet", "Er")
#print(asker.isim,asker.güç)
asker.hareket_et()

işçi = İşçi("Mehmet", "Usta")
#print(işçi.isim,işçi.güç)
işçi.hareket_et()

yonetici = Yönetici("Ali", "Takım Lideri")
#print(yonetici.isim,yonetici.güç)
yonetici.hareket_et()





