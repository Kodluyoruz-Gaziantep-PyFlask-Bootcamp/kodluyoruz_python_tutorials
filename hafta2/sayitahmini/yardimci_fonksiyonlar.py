import random

def get_distance_message(number,guess):

	messages = [
		(0,"Buldunuz"),
		(5,"Nerdeyse buldun"),
		(12,"Çok Yakın"),
		(18,"Yakın"),
		(25,"Az Uzak"),
		(30,"Uzak"),
		(40,"Çok Uzak"),
	]
	diff = number-guess

	message = ""
	if diff!=0:
		message = "Daha küçük giriniz : " if diff<0 else "Daha büyük giriniz : "

	for x in messages:
		if abs(diff)<=x[0]:
			message += x[1]
			break

	return message


def generate_number(start,end):
	return random.randint(start,end)

def get_input():
	return input("Lütfen tahmin ettiğiniz sayıyı giriniz : ")


def str_is_integer(value):
	return value.isdigit()
