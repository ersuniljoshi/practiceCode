import myQueue


# Hot potato problem
def implementationOfJosephus(nameList, times):
    q = myQueue.Queue()
    for value in nameList:
        q.Nqueue(value)

    while q.size() > 1:
        for i in range(times):
            import pudb
            pudb.set_trace()  # XXX BREAKPOINT
            q.Nqueue(q.Dqueue())
        q.Dqueue()

    return q.Dqueue()

names = ['sunil', 'soni', 'DPJ', 'Urmila', 'Pratibha', 'Dinesh', 'Advik', 'GC', 'Santosh', 'Pankaj']
print('Last Person left: {}'.format(implementationOfJosephus(names, 10)))
