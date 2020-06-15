from hafta2.matematik_islemleri_modulu import *
from hafta2.yardimci_fonksiyonlar import turleri_yazdir


def hesapmakinesi():

	while True:
		hesaplanacak_islem = input("İşlemi giriniz. (örn: 10+5) : ")
		ilk_sayi,islem_turu,ikinci_sayi = islem_degerlerini_bul(hesaplanacak_islem)

		if islem_turu=="hatali":
			print("Lütfen işlemi doğru giriniz!")
			continue

		#print(type(ilk_sayi),type(islem_turu),type(ikinci_sayi))
		#turleri_yazdir(ilk_sayi,islem_turu,ikinci_sayi)

		sonuc = hesapla(ilk_sayi,islem_turu,ikinci_sayi)
		cikti_mesaji = "{}{}{} = {:.2f}"
		if sonuc.is_integer():
			cikti_mesaji = "{}{}{} = {}"
			sonuc = int(sonuc)

		print(cikti_mesaji.format(ilk_sayi,islem_turu,ikinci_sayi,sonuc))

		devam_etsin_mi = input("Devam etmek istiyor musunuz? (Y/N) : ")
		if devam_etsin_mi.upper()=="N":
			break

