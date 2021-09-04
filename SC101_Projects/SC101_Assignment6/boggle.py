"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	game = []			# store boggle in list
	game_set = set()
	not_illegal = True		# If inputs are illegal or not.
	for i in range(1, 5):
		if not_illegal:

			# convert input(case-insensitive) into list
			row = list(map(lambda s: s.lower(), input(f"{i} row of letters: ").strip().split()))

			# find out if any of the inputs is illegal.
			for ele in row:
				if not ele.isalpha() or len(ele) != 1:
					not_illegal = False
					print('Illegal input')
					break

			# store the letters that appear in inputs.
			game_set = game_set.union(set(row))
			game.append(row)

	# the lines below are the demo boggle game

	# game = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]
	# for ele in game:
	# 	game_set = game_set.union(set(ele))

	if not_illegal:

		# read dictionary
		dictionary = read_dictionary(game_set)

		start = time.time()
		####################
		#                  #
		#       TODO:      #
		#                  #
		####################

		ans_lst = []		# store answers
		for i in range(4):
			for j in range(4):
				# words = [game[i][j]]		# determine the first pick, store as list
				words = game[i][j]		# determine the first pick, store as string（faster）
				find_words(game, words, [(i, j)], dictionary, ans_lst)

		print(f'There are {len(ans_lst)} words in total.')

		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary(game_set):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dictionary = []
	append = dictionary.append
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()		# eliminate '/n'

			# store words that are longer than 4 letters and are possible to find in the specific game
			if len(word) >= 4 and set(word).issubset(game_set):
				append(word)
	return dictionary


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dictionary: (list) a list contains all the words
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


# The lines belows are slower（ans: list）

# def find_words(game, ans, path, dictionary, ans_lst):
# 	if not has_prefix(''.join(ans), dictionary):
# 		pass
# 	else:
# 		position = path[-1]
# 		for i in range(-1, 2):
# 			if 0 <= position[0] + i < 4:
# 				for j in range(-1, 2):
# 					if 0 <= position[1] + j < 4:
# 						new_x = position[0] + i
# 						new_y = position[1] + j
# 						new_position = (new_x, new_y)
# 						if new_position not in path:
# 							ans.append(game[new_x][new_y])
# 							path.append(new_position)
# 							if len(ans) >= 4:
# 								word = ''.join(ans)
# 								if word in dictionary and word not in ans_lst:
# 									print(f'Found: {word}')
# 									ans_lst.append(word)
# 							find_words(game, ans, path, dictionary, ans_lst)
# 							ans.pop()
# 							path.pop()


def find_words(game, ans, path, dictionary, ans_lst):
	"""
	:param game: (list) our input.
	:param ans: (str) current word that is being examined.
	:param path: (list of tuple) the positions that are already used.
	:param dictionary: (list) list of all words
	:param ans_lst: (list) store all the answers that have been found
	"""
	# base-case
	if not has_prefix(ans, dictionary):
		pass

	else:
		position = path[-1]		# find the latest position that has been picked

		# find neighbors
		for i in range(-1, 2):
			if 0 <= position[0] + i < 4:
				for j in range(-1, 2):
					if 0 <= position[1] + j < 4:

						# choose new position that will be examined
						new_x = position[0] + i
						new_y = position[1] + j
						new_position = (new_x, new_y)

						# if the new position haven't been picked
						if new_position not in path:
							path.append(new_position)		# set new position as current position

							# determine if ans meets criteria
							if len(ans) >= 4:
								if ans in dictionary and ans not in ans_lst:
									print(f'Found: {ans}')
									ans_lst.append(ans)

							# recursion
							find_words(game, ans + game[new_x][new_y], path, dictionary, ans_lst)

							# un-choose
							path.pop()


# f y c l
# i o m g
# o r i l
# h j h u

if __name__ == '__main__':
	main()
