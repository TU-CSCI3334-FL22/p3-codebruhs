class Token:
    type = ""
    lexeme = ""

class Grammar:
    productions = []
    nonterminals = []
    terminals = []

class Tables:
    firstTable = {}
    followTable = {}
    nextTable = {}


def grammar_scan(contents):
    print("Scan contents into a list of tokens return it")
    return scan(contents)

def scan(contents):
    dict = {
        ";": "SEMICOLON",
        ":": "DERIVES",
        "|": "ALSODERIVES",
        "Epsilon": "EPSILON",
        "epsilon": "EPSILON",
        "EPSILON": "EPSILON",
    }

    words = contents.split()
    scanned = []
    
    for word in words:
        #if word[0] == "/" and word[1] == "/":
            #continue
        if word in dict:
            temp = Token()
            temp.type = dict[word]
            temp.lexeme = word
            scanned.append(temp)
        else:
            dict[word] = "SYMBOL"
            temp = Token()
            temp.type = dict[word]
            temp.lexeme = word
            scanned.append(temp)
    
    #print("Hello World")
    #print(dict)
    #for token in scanned:
        #print(token.type+", "+token.lexeme)
    return scanned

def grammar_parse(tokens):
    print("Read tokens into a grammar")
    return Grammar()

def fixLL(ir):
    return ir

def make_tables(ir, worklist):
    tables = Tables()
    if(worklist):
        sys.exit("Worklists not supported yet!")
    else:
        print("Make and return the appropriate tables")
        # Each Table is a Dictionary of Tokens mapped to Sets of Tokens
        tables.firstTable = makeFirst(ir)
        tables.followTable = makeFollow(ir, tables.firstTable)
        return(tables)

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

def print_tables(tables):
   print("Print tables in human-readable format")

def print_yaml(tables):
    print("Print tables in yaml format, or error if the involution of the next table fails")
   
