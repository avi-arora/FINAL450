# Definition for singly-linked list.
class ListNode:
    def __init__(self, x = 0, next=None):
        self.val = x
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pass

    def getIntersectionNodeBruteForce(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        TC: O(N*M) -> O(N^2)
        SC: O(1)
        """
        temp = headA
        while temp:
            itr = headB
            while itr:
                if temp == itr:
                    return temp.val
                itr = itr.next
            temp = temp.next
        return None

    def getIntersectionNodeHashTable(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        TC: O(N+M) -> O(N)
        SC: O(N)
        """
        table = {}
        temp = headA
        while temp:
            table[temp] = 0
            temp = temp.next
        
        temp = headB
        while temp:
            if temp in table:
                return temp.val
            temp = temp.next
        
        return None

            



if __name__ == "__main__":
    intersection = ListNode(8,ListNode(4, ListNode(5)))
    headA = ListNode(4,ListNode(1,intersection))
    headB = ListNode(5,ListNode(6,ListNode(1,intersection)))

    obj = Solution()
    print(obj.getIntersectionNodeHashTable(headA, headB))
    print(obj.getIntersectionNodeBruteForce(headA, headB))
