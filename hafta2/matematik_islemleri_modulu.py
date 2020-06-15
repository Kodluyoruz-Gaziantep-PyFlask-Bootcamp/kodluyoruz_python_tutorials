from operator import add,sub,mul,truediv,mod
from hafta2.yardimci_fonksiyonlar import string_float_mi,stringi_floata_donustur


def topla(ilk_sayi,ikinci_sayi):
	return add(ilk_sayi,ikinci_sayi)

def cikar(ilk_sayi,ikinci_sayi):
	return sub(ilk_sayi,ikinci_sayi)

def carp(ilk_sayi,ikinci_sayi):
	return mul(ilk_sayi,ikinci_sayi)

def bol(ilk_sayi,ikinci_sayi):
	return truediv(ilk_sayi,ikinci_sayi)

def kalani_bul(ilk_sayi,ikinci_sayi):
	return mod(ilk_sayi,ikinci_sayi)


islem_turleri = {
	"+" : topla,
	"-" : cikar,
	"*" : carp,
	"/" : bol,
	"%" : kalani_bul
}


def islem_degerlerini_bul(islem_metni):
	dizi = ["0","+","0"]

	for _islem_turu in islem_turleri.keys():
		if _islem_turu in islem_metni:
			dizi = list(islem_metni.partition(_islem_turu))
			break
		else:
			pass

	if not string_float_mi(dizi[0]) or not string_float_mi(dizi[2]):
		dizi[1] = "hatali"
		dizi[0] = 0
		dizi[2] = 0

	# eğer sıfıra bölünme işlemiyse hata ver
	if dizi[1]=="/" and dizi[2]=="0":
		dizi[1] = "hatali"

	return ( stringi_floata_donustur(dizi[0]), dizi[1], stringi_floata_donustur(dizi[2]) )



def hesapla(ilk_sayi,islem_turu,ikinci_sayi):
	sonuc = islem_turleri[islem_turu](ilk_sayi,ikinci_sayi)
	return float(sonuc)







__all__ = ["islem_degerlerini_bul","hesapla"]



