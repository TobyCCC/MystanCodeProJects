"""
File: extension.py
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        ##################
        #                #
        #      TODO:     #
        #                #
        ##################
        response = requests.get(url)
        html = response.text

        soup = BeautifulSoup(html, "html.parser")
        items = soup.find_all('tbody')          # find<tbody>

        for item in items:
            words = item.text.split()[:5 * 200]     # find words in relevance to rank, names, and populations
            count_male = 0
            count_female = 0
            for i in range(2, len(words), 5):       # find words in relevance to male populations
                num = ''
                for alp in words[i]:            # eliminate ',' between numbers
                    if alp.isdigit():
                        num += alp
                count_male += int(num)
            for i in range(4, len(words), 5):       # find words in relevance to female populations
                num = ''
                for alp in words[i]:
                    if alp.isdigit():
                        num += alp
                count_female += int(num)
        print(f'Male Number: {count_male}')
        print(f'Female Number: {count_female}')








if __name__ == '__main__':
    main()
