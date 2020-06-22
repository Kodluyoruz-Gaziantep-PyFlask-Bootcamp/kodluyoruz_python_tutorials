import random
from yardimci_fonksiyonlar import get_distance_message,generate_number,get_input,str_is_integer

def play_game():

	number = generate_number(1,100)
	while True:
		guess = get_input()
		if not str_is_integer(guess):
			print("Lütfen geçerli bir sayı giriniz")
			continue
		guess = int(guess)

		message = get_distance_message(number,guess)
		print(message)

		if message!="Buldunuz":
			continue

		action = input("Yeni oyun oynamak ister misiniz ? E/H")
		if action.upper()=="E":
			number = generate_number(0,100)
			print("Yeni oyun başladı")
		else:
			break




play_game()