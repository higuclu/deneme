def func(t):
    dic = {"{": "}", "(": ")", "[": "]"}
    stack = []
    for i in t:
        if i in "{[(":
            stack.append(i)
        elif stack and i == dic[stack[-1]]:
            stack.pop()
        else:
            return False
    return len(stack) == 0
t="[{{}}()(())]"
print(func(t))