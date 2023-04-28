from typing import Optional
from copy import deepcopy

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    cur = head
    while cur:
        print(cur.val, end=' -> ')
        cur = cur.next
    print('None')


def main():
    # 用例1:
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print_list(head)

    # h2 = head
    # h2.next = None
    # print_list(head)
    # print_list(h2)

    h3 = deepcopy(head)
    h3.next = None
    print_list(head)
    print_list(h3)



if __name__ == '__main__':
    main()