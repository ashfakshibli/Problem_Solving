def is_matched(expression):
    brackets = { "(":")","{":"}", "[":"]" }
    keys = list(brackets.keys())
    stack = []
    for i in expression:
        if (i in keys):
            stack.append(brackets[i])
        else:
            if(stack[-1] == i):
                stack.pop()
    if len(stack) == 0:
        return True
    else: 
        return False

t = int(input().strip())
for a0 in range(t):
    
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
