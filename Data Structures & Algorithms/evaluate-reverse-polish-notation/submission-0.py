class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        res=0
        for num in tokens:
            if num not in "+-*/%":
                stack.append(int(num))
            else:
                b=stack.pop()
                a=stack.pop()
                if num == "+":
                    res = a + b
                    stack.append(res)
                elif num == "-":
                    res = a - b
                    stack.append(res)
                elif num == "*":
                    res = a * b
                    stack.append(res)
                elif num == "/":
                    res = int(a / b)
                    stack.append(res)
        return stack[-1]