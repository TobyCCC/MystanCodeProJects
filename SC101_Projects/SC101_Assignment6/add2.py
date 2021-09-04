"""
File: add2.py
Name:
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    #                     #
    #        TODO:        #
    #                     #
    #######################
    cur_l1 = l1
    cur_l2 = l2
    ans = None

    # plus the digits that both l1 and l2 have
    while cur_l1 is not None and cur_l2 is not None:
        if ans is None:         # if it is the first node.
            plus = cur_l1.val + cur_l2.val
            carry = plus // 10          # if plus is bigger than 10, then it needs carry
            ans = ListNode(plus % 10, None)
            cur = ans
        else:
            plus = cur_l1.val + cur_l2.val + carry
            carry = plus // 10
            cur.next = ListNode(plus % 10, None)
            cur = cur.next

        cur_l1 = cur_l1.next
        cur_l2 = cur_l2.next

    # if l1 is bigger than l2
    while cur_l1 is not None:
        plus = cur_l1.val + carry
        carry = plus // 10
        cur.next = ListNode(plus % 10, None)
        cur = cur.next
        cur_l1 = cur_l1.next

    # if l2 is bigger than l1
    while cur_l2 is not None:
        plus = cur_l2.val + carry
        carry = plus // 10
        cur.next = ListNode(plus % 10, None)
        cur = cur.next
        cur_l2 = cur_l2.next

    # if it needs carry in the last digits 
    if carry != 0:
        cur.next = ListNode(carry, None)

    return ans


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
