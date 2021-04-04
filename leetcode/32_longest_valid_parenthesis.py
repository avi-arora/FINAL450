class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        ")()())"
        Using stack
        """
        stack = [-1]
        i = 0
        result, current = 0, 0
        while i < len(s):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")" and len(stack) > 0:
                stack.pop()
                if len(stack) > 0:
                    current = i-stack[len(stack)-1]
                if len(stack) == 0 and i < len(s):
                    stack.append(i)
            if current > result:
                result = current
            i+=1
        return result
                


if __name__ == "__main__":
    obj = Solution()
    print(obj.longestValidParentheses(")()())"))
