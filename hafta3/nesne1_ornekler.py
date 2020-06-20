
# # Yöntem 1
# sesli_harfler = 'aeıioöuü'
# sayaç = 0

# kelime = input('Bir kelime girin: ')

# for harf in kelime:
#     if harf in sesli_harfler:
#         sayaç += 1

# mesaj = '{} kelimesinde {} sesli harf var.'
# print(mesaj.format(kelime, sayaç))
# # Yöntem 1





# # Yöntem 2
# sesli_harfler = 'aeıioöuü'
# sayaç = 0

# kelime = input('Bir kelime girin: ')

# def seslidir(harf):
#     return harf in sesli_harfler

# for harf in kelime:
#     if seslidir(harf):
#         sayaç += 1

# mesaj = '{} kelimesinde {} sesli harf var.'
# print(mesaj.format(kelime, sayaç))
# # Yöntem 2




# # Yöntem 3
# sesli_harfler = 'aeıioöuü'
# sayaç = 0

# kelime = input('Bir kelime girin: ')

# def seslidir(harf):
#     return harf in sesli_harfler

# def artır():
#     global sayaç
#     for harf in kelime:
#         if seslidir(harf):
#             sayaç += 1
#     return sayaç

# mesaj = '{} kelimesinde {} sesli harf var.'
# print(mesaj.format(kelime, artır()))
# # Yöntem 3


# # Yöntem 4
# sesli_harfler = 'aeıioöuü'
# sayaç = 0

# kelime = input('Bir kelime girin: ')

# def seslidir(harf):
#     return harf in sesli_harfler

# def artır(sss):
#     for harf in kelime:
#         if seslidir(harf):
#             sss += 1
#     return sss

# mesaj = '{} kelimesinde {} sesli harf var.'
# print(mesaj.format(kelime, artır(sayaç)))
# # Yöntem 4


# # Yöntem 5
# sesli_harfler = 'aeıioöuü'
# sayaç = 0

# def kelime_sor():
#     return input('Bir kelime girin: ')

# def seslidir(harf):
#     return harf in sesli_harfler

# def artır(sayaç, kelime):
#     for harf in kelime:
#         if seslidir(harf):
#             sayaç += 1
#     return sayaç

# def ekrana_bas(kelime):
#     mesaj = "{} kelimesinde {} sesli harf var."
#     print(mesaj.format(kelime, artır(sayaç, kelime)))

# def çalıştır():
#     kelime = kelime_sor()
#     ekrana_bas(kelime)
# çalıştır()
# # Yöntem 5


# # Yöntem 6
# import nesne1_modul1
# nesne1_modul1.çalıştır()
# # Yöntem 6


# Yöntem 7
class HarfSayacı:
	sesli_harfler = 'aeıioöuü'
	sayaç_sesli = 0
	sessiz_harfler = 'bcçdfgğhjklmnprsştvyz'
	sayaç_sessiz = 0
	kelime = ""

	def __init__(self):
		# self.sesli_harfler = 'aeıioöuü'
		# self.sayaç_sesli = 0
		# self.sessiz_harfler = 'bcçdfgğhjklmnprsştvyz'
		# self.sayaç_sessiz = 0
		print("__init__ çalıştı")

	def kelime_sor(self):
		return input('Bir kelime girin: ')

	def seslidir(self, harf):
		return harf in self.sesli_harfler

	def sessizdir(self, harf):
		return harf in self.sessiz_harfler

	def artır(self):
		for harf in self.kelime:
			if self.seslidir(harf):
				self.sayaç_sesli += 1
			elif self.sessizdir(harf):
				self.sayaç_sessiz += 1

		return (self.sayaç_sesli, self.sayaç_sessiz)

	def ekrana_bas(self):
		mesaj = "{} kelimesinde {} sesli {} sessiz harf var."
		sesli, sessiz = self.artır()
		print(mesaj.format(self.kelime, sesli, sessiz))

	def çalıştır(self):
		self.kelime = self.kelime_sor()
		self.ekrana_bas()


if __name__ == '__main__':
	sayaç = HarfSayacı()
	sayaç.çalıştır()
# Yöntem 7



