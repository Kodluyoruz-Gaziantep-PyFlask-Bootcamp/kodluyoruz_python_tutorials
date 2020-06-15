"""
bu modülün dökümantasyonu buraya yazılacak.
...
...
...
"""

def fonk1():
    print('fonk1')

def fonk2():
    print('fonk2')

def fonk3():
    print('fonk3')

def fonk4():
    print('fonk4')

def fonk5():
    print('fonk5')

def _fonk6():
    print('_fonk6')

def __fonk7():
    print('__fonk7')

def fonk8_():
    print('fonk8_')



__all__ = ['fonk1', 'fonk2', 'fonk3',"fonk8_"]

if __name__=="__main__":
	fonk1()
	__fonk7()
	print("test.py dosyası çalıştırıldı")


