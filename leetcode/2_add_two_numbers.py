# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Stack based solutions
        TC: O(m+n)
        SC: O(m+n)
        """
        s1, s2, = [], []

        #fill the stack
        temp = l1
        while temp:
            s1.append(temp.val)
            temp = temp.next
        temp = l2
        while temp:
            s2.append(temp.val)
            temp = temp.next
        
        #pop out from stack and compute 
        result = temp = None
        sum, carry = 0, 0
        while len(s1) > 0 and len(s2) > 0:
            sum = s1.pop() + s2.pop() + carry
            if sum > 9:
                sum, carry = sum%10, sum//10
            else:
                carry = 0
            node = ListNode(sum)
            if temp:
                temp.next = node
                temp = node
            else:
                temp = node
                result = temp
        
        #check which stack is non empty 
        while len(s1) > 0:
            sum = s1.pop() + carry
            if sum > 9:
                sum, carry = sum%10, sum//10
            else:
                carry = 0
            node = ListNode(sum)
            temp.next = node
            temp = node
        
        while len(s2) > 0:
            sum = s2.pop() + carry
            if sum > 9:
                sum, carry = sum%10, carry//10
            else: 
                carry = 0
            node = ListNode(sum)
            temp.next = node
            temp = node
        
        if carry != 0:
            node = ListNode(carry)
            temp.next = node
        
        return result


if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4,ListNode(9)))
    l2 = ListNode(5,ListNode(6,ListNode(4)))
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    t = result
    while t:
        print(t.val)
        t = t.next



