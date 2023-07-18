import requests
from bs4 import BeautifulSoup
from object import *
import os

def outfile(player: user):
	with open("player_info.txt","w") as file:
		file.write(player.get_name())
		file.write(str(player.get_point()))

def intro(string, character):
	width = len(character) - len(string)
	string = string.upper()
	print(character)
	print(string.center(width))
	print(character)


def get_source(url: str) -> list:
	"""
 Get an url then return the source word list
	"""
	response = requests.request("GET", url)
	soup = BeautifulSoup(response.text, "html.parser")
	#get the table and row
	table = soup.find_all("table")[0]
	word_lst = table.find_all("td")
	#turn all word to list
	word_lst = [
	 word.text for word in word_lst
	 if ("\n" not in word.text) and (word.text != None)
	]
	return word_lst


def guessing_game(vocab):
	#set arg
	ls_vocab = libary(vocab)
	player = user(input("username: "), 0)
	intro("guessing game", "-------------------------")

	#intro
	print(
	 "\n welcome to guessing vocab game\n rule is simple -> guess the exactly meaning of word in vienamese ->get point"
	)
	print(f"your point: {player.get_point()}")
	turn = int(input("how many turn play: "))

	#play
	for i in range(turn):
		print(f"turn {i}")
		correct = ls_vocab.get_word()
		ans = input(f"{correct.content} -> ")

		#check ans
		if (ans.strip() == str(correct.get_mean)):
			print("Correct! ")
			player.up_point()
			print("your point:", player.get_point())
		else:
			print("Wrong Answer")
		print(f"Word meaning: {correct.get_mean()}")
		outfile(player)
	print("finish, thanks for playing")


#Tras feature
def Trans_word(mode=0):
	intro("translation", "--------------------")
	language = {
	 "vietnamese [vi]": "vi",
	 "english [en]": "en",
	 "korean [ko]": "ko",
	 "japanese [ja]": "ja",
	 "chinese [zh-tw]": "zh-tw"
	}
	lan = language.keys()
	print("Languages:", " - ".join(lan))
	ans = Word(input("input word: "))
	if mode == 0:
		try:
			des = input("Trans into: ").lower()
		except des in "0123456789" or len(des) > 5:
			print("wrong format")
	else:
		des = "vietnamese"
	print(f"-> {ans.get_mean(des)}")


def Learn_vocab(vocab: libary):
	language = {
	 "vietnamese [vi]": "vi",
	 "english [en]": "en",
	 "korean [ko]": "ko",
	 "japanese [ja]": "ja",
	 "chinese [zh-tw]": "zh-tw"
	}
	lan = language.keys()
	print("languages:", " - ".join(lan))
	des = input("Translate from Eng into: ").lower()
	for i in vocab.get_source():
		print("{} - {}".format(i.content, i.get_mean(des)))
