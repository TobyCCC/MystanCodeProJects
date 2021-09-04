"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

dictionary = []


def main():
    """
    TODO:
    """

    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')

    while True:
        word = input('Find anagrams for: ')

        if word == '-1':        # Type '-1' to end this program
            break



        # build a list of words that are composed of same alphabet and same numbers of  alphabet
        read_dictionary(word)

        start = time.time()

        print('Searching...')
        ans = find_anagrams(word)
        print(f'{len(ans)} anagrams : {ans}')

        end = time.time()



    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(s):
    """
    This function build a list of words that are composed of same characters and same numbers of characters
    s: str, The word we input.
    """
    set_s = set(s)
    append = dictionary.append
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()         # eliminate '/n'
            # if set(word) == set_s and len(word) == len(s):
            if set(word) == set_s:      # This is a little bit faster than the upper one
                append(word)


def find_anagrams(s):
    """
    s: str, The word we input.

    return:
        ans: list, list of words meet the criteria.
    """
    list_s = list(s)        # alter the word（str） into a list consist of single alphabet
    ans = []
    helper(list_s, [], ans, [])
    return ans


def helper(s, test, ans, former_test):
    """
    :param s: list, The word we input.
    :param test: list, permutation that is testing
    :param ans: list, list of words meet the criteria.
    :param former_test: list, list of permutations that have been tested.
    """
    if s == []:
        found = ''.join(test)           # alter list into str

        # if we find the word in dictionary, then add to ans.（Avoid words that have been already in ans）
        if found in dictionary and found not in ans:
            ans.append(found)
            print(f'Found : {found}')
            print('Searching...')
    else:
        # choose
        for i in range(len(s)):
            test.append(s[i])
            s.pop(i)
            found = ''.join(test)

            # avoid examining same alignment(if there are same alphabets in the word)
            if found not in former_test:
                former_test.append(found)

                # if there is no such prefix in dictionary, stop finding word with the prefix
                if has_prefix(found):
                    # explore
                    helper(s, test, ans, former_test)
                    # un-choose
                    s.insert(i, test.pop())

                else:
                    s.insert(i, test.pop())

            else:
                s.insert(i, test.pop())


def has_prefix(sub_s):
    """
    :param sub_s: str, prefix that needs to be examined
    :return:
        boolean, if there is any word with specific prefix in dictionary.
    """
    for ele in dictionary:
        if ele.startswith(sub_s):
            return True
    else:
        return False


if __name__ == '__main__':
    main()
