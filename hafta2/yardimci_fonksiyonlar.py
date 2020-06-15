def turleri_yazdir(*args):
	for x in args:
		print(x ," = ", type(x))

def string_float_mi(str):
	try:
		float(str)
		return True
	except Exception as e:
		return False

def stringi_floata_donustur(str):
	if string_float_mi(str):
		return float(str)
	else:
		return float(0)