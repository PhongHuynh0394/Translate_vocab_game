import random
from googletrans import Translator


#word
class Word:

	def __init__(self, content: str):
		self.content = content

	def get_mean(self, des="vi"):
		translator = Translator()
		return translator.translate(self.content, dest=des).text


#libary have many word
class libary:
	__source = []

	def __init__(self, word_list: list):
		self.__source = [Word(i) for i in word_list if i != ""]

	def get_word(self) -> Word:
		ran_num = random.randint(0, len(self.__source) - 1)
		return self.__source[ran_num]

	def get_source(self):
		return self.__source


#user
class user:
	__name: str
	__point: int

	def __init__(self, name, point):
		self.__name = name
		self.__point = point

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name

	def get_point(self):
		return self.__point

	def set_point(self, point):
		self.__point = point

	def up_point(self):
		self.__point += 1

	def reset(self):
		self.__point = 0
		self.__name = None


# def GiveWord(word_lst, trans="vi"):
# 	'''
# return word and its translation default in vietnam
#  '''
#   translator = Translator()
#   ran = random.randint(0, len(word_lst)-1)
#   word = word_lst[ran]
#   return word, translator.translate(word, dest=trans).text
