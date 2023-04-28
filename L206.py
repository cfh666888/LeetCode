# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        # if head.val == 0:
        #     print("[]")
        #     return None
        # if head.next == None:
        #     print("[" + str(head.val) + "]")
        #     return None
        if head == None or head.next == None:
            return head
        bef = head
        cur = head.next
        nex = cur.next
        #防止死循环，第一个节点不再指向第二个节点，而指向空
        bef.next = None
        while cur != None:
            cur.next = bef
            bef = cur
            cur = nex
            if nex != None:
                nex = nex.next
        return bef
        # print("[", end="")
        # while bef != None:
        #     if bef.next != None:
        #         print(bef.val, end=",")
        #     else:
        #         print(bef.val, end="")
        #     bef = bef.next
        # print("]")



if __name__ == '__main__':
    s = Solution()

    head = ListNode(1)
    s.reverseList(head)
