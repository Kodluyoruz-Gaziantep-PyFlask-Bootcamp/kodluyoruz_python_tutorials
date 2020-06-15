moduller = ['os', 'sys', 'random',"subprocess"]

def kesisim_bul(moduller):
	# kumeler = [set(dir(__import__(modul))) for modul in moduller] #aşağıdaki for ile aynı işi tek satırda yapar
	kumeler = []
	for modul in moduller:
		kumeler.append(set(dir(__import__(modul))))

	return set.intersection(*kumeler)


if __name__=="__main__":
	print(kesisim_bul(moduller))
	print(__name__)
