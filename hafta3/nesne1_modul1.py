# Yöntem 5
sesli_harfler = 'aeıioöuü'
sayaç = 0

def kelime_sor():
    return input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler

def artır(sayaç, kelime):
    for harf in kelime:
        if seslidir(harf):
            sayaç += 1
    return sayaç

def ekrana_bas(kelime):
    mesaj = "{} kelimesinde {} sesli harf var."
    print(mesaj.format(kelime, artır(sayaç, kelime)))

def çalıştır():
    kelime = kelime_sor()
    ekrana_bas(kelime)
