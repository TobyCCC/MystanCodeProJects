"""
This program is used for examining problem 1
"""


def main():
    base_case = [0]         # count how many times are base case reached
    num = b(5, 2, base_case)
    print(num)
    print(*base_case)


def b(n, k, base_case):
    """
    :param n: int
    :param k: int
    :param base_case: list
    :return: int
    """
    if k == 0 or k == n:
        print('base case!')
        base_case[0] += 1
        return 2
    else:
        return b(n-1, k-1, base_case) + b(n-1, k, base_case)


if __name__ == '__main__':
    main()