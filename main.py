from func import *
from object import *
import os


def menu():
	os.system('clear')
	url = "https://www.pass-the-toeic-test.com/toeic-word-list.php"
	while True:
		intro = """
menu feature:
1. Guessing game
2. Translate
3. Learn vocab
0. exit
	 """
		word_lst = get_source(url)
		vocab = libary(word_lst)
		print(intro)
		choice = int(input("your choice: "))
		if choice == 1:
			guessing_game(word_lst)
		elif choice == 2:
			Trans_word()
		elif choice == 3:
			Learn_vocab(vocab)
		elif choice == 0:
			print("Thanks for using")
			break

		choice = input("Do you want to finish [Y/n]: ")
		#finish
		if choice.lower() in ["y", "yes"]:
			print("Thanks for using")
			break
		
if __name__ == "__main__":
	menu()