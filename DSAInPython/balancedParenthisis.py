import myStack

def matches(close,open):
    sampleOpen = "({["
    sampleClose = ")}]"
    return sampleClose.index(close) == sampleOpen.index(open)

def matchParenthesis(exp):
    s = myStack.Stack()
    balanced = True
    for sym in exp:
        if sym in "({[":
            s.push(sym)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(sym,top):
                    balanced = False
    return balanced

print str(matchParenthesis("a"))

