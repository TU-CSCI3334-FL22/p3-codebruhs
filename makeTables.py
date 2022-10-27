from multiprocessing.sharedctypes import Value
from mbnfScanner import Token
from mbnfParser import Grammar

def makeFirst(ir):
    first = {}
    epToken = "EPSILON"

    print("Create First Table:")
    for alpha in ir.terminals:
        first[alpha] = {alpha}
    first[epToken] = {"EPSILON"}
    # If we need something for eof, put that here
    for a in ir.nonterminals:
        first[a] = set()
    
    # Add Epsilon to empty lists
    for prod in ir.productions:
        if len(prod[1]) == 0:
            prod[1].append("EPSILON")

    firstChanged = True
    oldFirst = copyTable(first)
    emptySet = set()
    while firstChanged == True:
        firstChanged = False
        rhs = set()
        for prod in ir.productions:
            #print(prod)
            b1 = prod[1][0] # first result in production 
            rhs = first[b1].copy()
            if epToken in rhs:
                rhs.remove(epToken)
            i = 0
            k = len(prod[1]) - 1
            while epToken in first[prod[1][i]] and i < k:
                i += 1
                temp = first[prod[1][i]].copy()
                rhs = rhs.update(temp.remove(epToken))
            if i == k and epToken in first[prod[1][k]]:
                rhs.add(epToken)
            first[prod[0]].update(rhs)
            #print("Production done")
        # Need to Check if first has changed
        for key in first:
            if (len(first[key].difference(oldFirst[key])) != 0):
                # Difference is not 0, something has changed
                firstChanged = True
        oldFirst = copyTable(first)

    return first

def makeFollow(ir, first):
    follow = {}
    epToken = "EPSILON"
    eofToken = "EOF"

    print("Create Follow Table:")
    for a in ir.nonterminals:
        follow[a] = set()
    #Incorrect - need a better way of finding top-level production (not always at top)
    s = ir.productions[0][0]
    follow[s] = {eofToken}

    followChanged = True
    oldFollow = copyTable(follow)
    while followChanged == True:
        followChanged = False
        for prod in ir.productions:
            trailer = follow[prod[0]].copy()
            k = len(prod[1]) - 1
            for i in range(k, -1, -1):
                bi = prod[1][i]
                if bi in ir.nonterminals:
                    follow[bi].update(trailer)
                    if epToken in first[bi]:
                        trailer.update(first[bi])
                        #print(follow)
                        trailer.remove(epToken)
                    else:
                        trailer = first[bi].copy()
                else:
                    trailer = first[bi].copy() # Bi is a terminal
        # Need to Check if follow has changed
        for key in follow:
            if (len(follow[key].difference(oldFollow[key])) != 0):
                # Difference is not 0, something has changed
                followChanged = True
        oldFollow = copyTable(follow)

    return follow

def makeNext(ir, firstTable, followTable):
    print('Create Next Table: ')
    nextTable = {}
    epToken = "EPSILON"
    eofToken = "EOF"
    for i in range(len(ir.productions)):
        production = ir.productions[i]
        head = production[0]
        #print('')
        #print(production)
        #print(followTable[head])

        firstEpsilons = False
        for terminal in production[1]:
            if epToken in firstTable[terminal]:
                firstEpsilons = True
        nextSet = set()

        if (firstEpsilons):
            # Next(A -> Bs) = First(all Bs) union Follow(A)
            nextSet.update(followTable[head])
            for terminal in production[1]:
                nextSet.update(firstTable[terminal])
        else:
            # Next(A -> Bs) = First(Bs up to and including first non-epsilon B) minus Epsilon
            i = 0
            k = len(production[1])
            nonEpsilonFound = False
            while i < k and not(nonEpsilonFound):
                if production[1][i] == "EPSILON":
                    i = i+1
                else:
                    nonEpsilonFound = True
                    nextSet.update(firstTable[production[1][i]])
            if epToken in nextSet:
                #print('Removing Epsilon')
                nextSet.remove(epToken)
        #print(newThing)
        nextTable[(production[2], production[0])] = nextSet
    #print('\nNextTable:')
    #for production in next:
        #print(production)
    return nextTable

def unionSets(baseSet, inputSet):
    out = []
    for value in baseSet:
        out.append(value)
    for value in inputSet:
        if not value in out:
            out.append(value)
    return out

def copyTable(dict):
    # For some reason the .copy() function only makes a shallow copy when used on the tables
    newDict = {}
    for key in dict:
        newDict[key] = dict[key].copy()
    return newDict