from mbnfParser import Grammar

def rmDirLeftRecursion(ir):
    # Group productions into non-recursive A -> b and recursive A -> A a
    nonRecursive = []
    recursive = []
    hasRecursiveProd = []
    for prod in ir.productions:
        startNT = prod[0]
        # Find first non-terminal in rhs
        i = 0
        k = len(prod[1]) - 1
        nonTerminalFound = False
        while not(nonTerminalFound) and i <= k:
            if prod[1][i] in ir.nonterminals:
                print("prod[1][i] = "+ prod[1][i])
                print("startNT = "+ startNT)
                if prod[1][i] == startNT:
                    recursive.append((prod, i))
                    hasRecursiveProd.append(startNT)
                else:
                    nonRecursive.append(prod)
                nonTerminalFound = True
            else:
                i = i+1
        print(i)
        if not(nonTerminalFound):
            nonRecursive.append(prod)

    print("Non-recursive productions: ")
    print(nonRecursive)
    print("Recursive productions: ")
    print(recursive)
    print("These Non-Terminals have recursive productions: ")
    print(hasRecursiveProd)
    
    # Replace all productions of the form (A -> b) with A -> b A'
    for prod in nonRecursive:
        startNT = prod[0]
        if prod[0] in hasRecursiveProd:
            ntPrime = startNT + "'"
            ir.nonterminals.append(ntPrime)
            prod[1].append(ntPrime)
    
    # Replace all productions of the form (A -> A a) with A' -> a A'
    llRecursiveProds = []
    for (prod, i) in recursive:
        startNT = prod[0]
        prod[1].pop(i)
        ntPrime = startNT + "'"
        prod[1].append(ntPrime)
        llRecursiveProds.append(prod)
    
    # Add A' -> Epsilon
    numProductions = len(ir.productions)
    for nt in hasRecursiveProd:
        ntPrime = nt + "'"
        numProductions = numProductions + 1
        llRecursiveProds.append((ntPrime, ["EPSILON"], numProductions))
    
    newIr = Grammar()
    newIr.productions = nonRecursive + llRecursiveProds
    newIr.nonterminals = ir.nonterminals
    newIr.terminals = ir.terminals
    return newIr