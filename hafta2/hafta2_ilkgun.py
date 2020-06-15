#import os
#import os as ahmet
#from os import name,getcwd
from os import name as na
# from os import getcwd
#from os import *
# os = __import__("os")



# print(dir(os))
#print(os.name)
#print(os.getcwd())

print(na)
#print(name)
# print(getcwd())


def fonkimport():
	from os import getcwd
	# from os import * # hata verir, bu şekilde dosya başında import edilmeli
	print(getcwd())

fonkimport()



# isim = input("isminiz: ")
# print(isim)
# soyisim = input("soyisminiz: ")
# print(soyisim)


def topla(ilksayi,ikincisayi):
	sonuc = ilksayi+ikincisayi
	return sonuc

def cikar(ilksayi,ikincisayi):
	return ilksayi-ikincisayi

def carp(ilksayi,ikincisayi):
	return ilksayi*ikincisayi

def bol(ilksayi,ikincisayi):
	return ilksayi/ikincisayi


ilksayi = 0
ikincisayi = 0
islem = "+"

# while ilksayi!="cikis":
while True:

	ilksayi = input("İlk sayıyı giriniz : ")
	if ilksayi=="cikis":
		break

	# if ilksayi=="cikis":
	# 	continue

	ilksayi = int(ilksayi)
	# print(type(ilksayi))
	islem = input("İşlemi giriniz [+,-,*,/] : ")
	ikincisayi = int(input("İkinci sayıyı giriniz : (Çıkmak için cikis yaziniz)"))

	sonuc = 0
	if islem=="+":
		# sonuc = ilksayi+ikincisayi
		sonuc = topla(ilksayi,ikincisayi)
	elif islem=="-":
		sonuc = cikar(ilksayi,ikincisayi)
	elif islem=="*":
		sonuc = carp(ilksayi,ikincisayi)
	elif islem=="/":
		sonuc = bol(ilksayi,ikincisayi)
	else:
		print("Hatalı işlem türü")

	# print("Sonuç = " + str(sonuc))
	# print("Sonuç = " , sonuc)
	# print(str(ilksayi) + islem + str(ikincisayi) + " = " + str(sonuc))
	#print("%% %s %s %s = %s" % (ilksayi,islem,ikincisayi,sonuc))
	#print("%d %s %d = %f" % (ilksayi,islem,ikincisayi,sonuc))
	#print("%d %s %d = %.2f" % (ilksayi,islem,ikincisayi,sonuc))
	#print("{1} {0} {2} = {3}".format(islem,ilksayi,ikincisayi,sonuc))
	print("{1} {0:s} {2:d} = {3:.2f}".format(islem,ilksayi,ikincisayi,sonuc))


print("%15s" % "istihza")
print("istihza".rjust(15))
print("%-15s" % "istihza")
print("istihza".ljust(15))


print("depoda %(miktar)s kilo %(ürün)s kaldı" % {"miktar": 25, "ürün": "elma"})
print("depoda %s kilo %s kaldı" % (25,"elma"))
print("sayı = %d" %23)
print("sayı = %10.5d" %23)



print("{0} {1} ({1} {0})".format("Serkan", "Dağlıoğlu"))
print("{dil} dersleri, {dil2} dersleri".format(dil="python", dil2="Java"))
print("{:,}".format(1234567890))



# a = 1
# while a<10:
# 	print(a)
# 	a += 1

# print("----------------------")

# a = 1
# while a<100:
# 	if a%2==0:
# 		print(a)
# 	a+=1



tr_harfler = "şçöğüİı"

a = 0
while a < len(tr_harfler):
    print(tr_harfler[a], sep="\n")
    a += 1


print("----------------------")

for harf in tr_harfler:
	print(harf)

print("----------------------")

for sayi in range(5,25):
	print(sayi)

print("----------------------")
for sayi in range(10):
	print(sayi)


print("----------------------")
for sayi in range(0,24,3):
	print(sayi)

print("----------------------")
for sayi in range(10,0,-1):
	if sayi==0:
		pass
	else:
		print(sayi)


print("----------------------")
for sayi in range(0,10):
	if sayi>5:
		break

	print(sayi)

print("----------------------")
for sayi in range(0,10):
	if sayi>5 and sayi<8:
		continue

	print(sayi)


x = 0
while x<20:
	x = int(input("Sayı girin (cikis için 5 giriniz)"))
	if x==5:
	 	break
	print(x)
else:
	print("else çalıştı.")


nullDegisten = None




print("FONKSİYONLAR")

def kayit_olustur(isim, soyisim, email="Boş", telefon="Boş"):
	print("Yeni Kayıt : ")
	print("%s %s | email=%s | telefon=%s" % (isim,soyisim,email,telefon))


kayit_olustur("Serkan","Dağlıoğlu","serkandaglioglu@gmail.com","5064485669")
#kayit_olustur("Serkan2","Dağlıoğlu2","serkandaglioglu2@gmail.com","50644856692")
#kayit_olustur("Serkan3","Dağlıoğlu3","serkandaglioglu3@gmail.com","50644856693")
kayit_olustur(soyisim="Dağlıoğlu",isim="Serkan",email="serkandaglioglu@gmail.com", telefon="5064485669")
kayit_olustur("Serkan", "Dağlıoğlu","serkandaglioglu@gmail.com")




islemsonucu1 = topla(1,2)
print(islemsonucu1)

islemsonucu2 = cikar(10,5)
print(islemsonucu2)

def uzunluk(oge):
    c = 0
    for s in oge:
        c += 1
    return c

print(uzunluk("serkan dağlıoğlu"))
# print(len("serkan dağlıoğlu")) // üstteki satır ile aynı sonucu verir


print("-------------------------")
def sayisiz_parametreli_fonksiyon(*args):
	print(args)
	for a in args:
		print(a)

sayisiz_parametreli_fonksiyon("a","b","c","d")
sayisiz_parametreli_fonksiyon("x","y")
sayisiz_parametreli_fonksiyon("x")
sayisiz_parametreli_fonksiyon(1,2,4,5,6,7,89,77,5,3,37)

dizi1 = ["a","b","c","d",1,2,3]
sayisiz_parametreli_fonksiyon(*dizi1)




def sayisiz_isimli_parametreleri_fonksiyon(**kwargs):
	print(type(kwargs))
	print(kwargs)


sayisiz_isimli_parametreleri_fonksiyon(param1="Serkan",
	param2="Dağlıoğlu",
	param3="Kodluyoruz")


def kayit_olustur_kwargs(**kwargs):
	print(kwargs)
	print("%s %s | email=%s | telefon=%s" % (kwargs["isim"],kwargs["soyisim"],kwargs["email"],kwargs.get("telefon","Boş")))

sozluk1 = { "isim" : "Serkan" ,
		"soyisim" : "Dağlıoğlu",
		"email" : "serkandaglioglu@gmail.com"
	}
kayit_olustur_kwargs(**sozluk1)


def fonk(param1, param2):
	return param1 + param2

fonk_lambda = lambda param1, param2: param1 + param2

print(fonk(1,2))
print(fonk_lambda(1,2))



#harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
#cevrim = {i: harfler.index(i) for i in harfler}

isimler = ["ahmet", "ışık", "ismail", "çiğdem",
           "can", "şule", "iskender"]

birlestir = lambda dizi1,ayirici : ayirici.join(dizi1)
# def birlestir(dizi1,ayirici):
# 	return ayirici.join(dizi1)
# print(birlestir(isimler, ","))


def fonksiyon_parametreli(dizi1,ayirici,fonkparam1):
	return fonkparam1(dizi1,ayirici)

print(fonksiyon_parametreli(isimler,",", birlestir))


def fonk_icinde_fonk():
	def icerideki_fonk():
		print("icerideyim")
	icerideki_fonk()

fonk_icinde_fonk()
# icerideki_fonk() # hata verir







