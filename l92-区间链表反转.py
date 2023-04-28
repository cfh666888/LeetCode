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


class Solution:
    def print_list(self, head):
        cur = head
        while cur:
            print(cur.val, end=' -> ')
            cur = cur.next
        print('None')

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # 1. 找到left节点的前一个节点pre_left,以及right节点的后一个节点post_right。这是为了在反转后正确拼接链表。
        len = 0
        h1 = head
        #求出链表长度
        while h1 != None:
            len += 1
            h1 = h1.next
        # print("链表长度",len)
        # print(h1) #None
        # print(head.val) #1
        if len == 1 or left == right:
        # if len == 1:
            return head
        #特殊情况
        if left == 1:
            pre_left = None
        if right == len:
            post_right = None

        #一般情况
        h2 = head
        curPos = 1
        while h2 != None:
            if curPos == left - 1:
                pre_left = h2
            if curPos == right + 1:
                post_right = h2
            h2 = h2.next
            curPos += 1
        #测试找对了没
        # print("左边之前的")
        # print_list(pre_left)
        # print("右边之后的")
        # print_list(post_right)

        # 2. 从left节点开始反转到right节点,得到reversed_list。这一步就是反转链表的典型实现。
        # 2.1先取出来中间这一段
        h2 = deepcopy(head)
        # print_list(h2)
        curPos = 1
        while h2 != None:
            if curPos == left:
                newHead = h2
                tailNewHead = newHead.next
            if curPos > left and curPos < right:
                tailNewHead = tailNewHead.next
            if curPos == right:
                tailNewHead.next = None
                break
            h2 = h2.next
            curPos += 1
        # print("---------")
        # print_list(newHead)
        # print_list(tailNewHead)
        # print("---------")
        # 2.2反转中间这一段即newHead
        if newHead.next == None:
            cur = newHead
        else:
            cur = newHead
            nex = cur.next
            #防止互相指
            cur.next = None
            #nex肯定不为None
            nexnex = nex.next
            while nex != None:
                nex.next = cur
                cur = nex
                nex = nexnex
                if nexnex != None:
                    nexnex = nexnex.next
        # print("=======")
        # print_list(cur)
        # print_list(newHead)
        # print("=======")


        # 3. pre_left->next = reversed_list,与前半部分链表拼接。
        if pre_left == None:    #防止pre_left为None
            head = cur
        else:
            pre_left.next = cur
        # 4. post_right->next = right->next,与后半部分链表拼接。
        newHead.next = post_right
        # print("部分反转后的")
        # print_list(head)
        # 5. right->next = NULL,防止链表环。
        return head





def main():
    # # 用例1:
    # head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    # solution = Solution()
    # solution.reverseBetween(head, 2, 4)
    # solution.print_list(head)

    # 用例2:
    # head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # solution = Solution()
    # head = solution.reverseBetween(head, 1, 2)
    # solution.print_list(head)

    # 用例3:
    # head = ListNode(5)
    # solution = Solution()
    # head = solution.reverseBetween(head, 1, 1)
    # solution.print_list(head)

    # 用例4:
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    solution = Solution()
    head = solution.reverseBetween(head, 1, 1)
    solution.print_list(head)


if __name__ == '__main__':
    main()