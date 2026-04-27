class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        check = []
        ans = 0
        for i in range(0, len(tokens)):
            if tokens[i] == '+':
                b = int(check.pop())
                a = int(check.pop())
                ans = a + b
                check.append(str(ans))
            elif tokens[i] == '-':
                b = int(check.pop())
                a = int(check.pop())
                ans = a - b
                check.append(str(ans))
            elif tokens[i] == '*':
                b = int(check.pop())
                a = int(check.pop())
                ans = a * b
                check.append(str(ans))
            elif tokens[i] == '/':
                b = int(check.pop())
                a = int(check.pop())
                ans = int(a / b)
                check.append(str(ans))
            else:
                check.append(tokens[i])
        return int(check[0])