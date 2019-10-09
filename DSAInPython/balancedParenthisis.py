import myStack
import os

sampleOpen = "({["
sampleClose = ")}]"

def matches(cl, op):
    return sampleClose.index(cl) == sampleOpen.index(op)

def matchParenthesis(exp):
    s = myStack.Stack()
    balanced = True
    for sym in exp:
        if sym in sampleOpen:
            s.push(sym)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(sym, top):
                    balanced = False
    return balanced

print(str(matchParenthesis("()a")))
