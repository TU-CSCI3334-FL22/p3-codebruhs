def makeFirst(ir):
    first = {}
    epToken = Token()
    epToken.type = "EPSILON"
    first[epToken] = {epToken}

    print("Create First Table:")
    for alpha in ir.terminals:
        first[alpha] = {alpha}
    # If we need something for eof, put that here
    for a in ir.nonterminals:
        first[a] = {}
        
    firstChanged = True
    oldFirst = first
    emptySet = {}
    while firstChanged == True:
        firstChanged = False
        rhs = {}
        for prod in ir.productions:
            b1 = prod[1] # first result in production 
            rhs = first[b1].remove(epToken)
            i = 1
            k = len(prod) - 1
            while epToken in first[prod[i]] and i < k:
                i += 1
                rhs = rhs.update(first[prod[i]].remove(epToken))
            if i == k and epToken in first[k]:
                rhs = rhs.add(epToken)
            first(prod[0]).update(rhs)
        # Need to Check if first has changed
        for key in first:
            if (len(first[key].difference(oldFirst[key])) != 0):
                # Difference is not 0, something has changed
                firstChanged = True
        oldFirst = first

    return first

def makeFollow(ir, first):
    follow = {}
    epToken = Token()
    epToken.type = "EPSILON"
    eofToken = Token()
    eofToken.type = "EOF"

    print("Create Follow Table:")
    for a in ir.nonterminals:
        follow[a] = {}
    s = ir.productions[0][0]
    follow[s] = {eofToken}

    followChanged = True
    oldFollow = follow
    while followChanged == True:
        followChanged = False
        for prod in ir.productions:
            trailer = follow[prod[0]]
            k = len(prod) - 1
            for i in range(k, 1, -1):
                bi = prod[i]
                if bi in ir.nonterminals:
                    follow[bi].update(trailer)
                    if epToken in first[bi]:
                        trailer.update(first[bi].remove(epToken))
                    else:
                        trailer = first[bi]
                else:
                    trailer = first[bi] # Bi is a terminal
        # Need to Check if follow has changed
        for key in follow:
            if (len(first[key].difference(oldFollow[key])) != 0):
                # Difference is not 0, something has changed
                followChanged = True
        oldFollow = follow

    return follow