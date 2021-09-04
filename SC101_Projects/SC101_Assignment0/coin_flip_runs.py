"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random as r


def main():
	"""
	TODO: This program is a coin flipping simulator. It will stop when the number or runs is reached.
	"""
	print("Let's flip a coin!")
	count = 0
	result = ""
	flip_origin = ""									# Store the result one round before.
	switch = 0											# Determine if a run includes more than two "H" or "T"
	num_run = int(input("Number of runs: "))
	while True:
		if count == num_run:
			break
		flip_num = r.randint(0,1)						# Random
		if flip_num == 0:
			flip = "H"
		else:
			flip = "T"
		result += flip
		if flip_origin == flip:
			if switch == 0:
				switch = 1
				count += 1
		else:
			switch = 0
		flip_origin = flip
	print(result)


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
