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
    if(worklist):
        sys.exit("Worklists not supported yet!")
    else:
        print("Make and return the appropriate tables")
        return(Tables())
"""
def make_next(ir,firstSet,followSet):
    epToken = Token()
    epToken.type = "EPSILON"
    i = 0
    while i < ir.length(): #make a for loop
        tok = ir(i)
        j = 0
        firstSets = first(tok)
        hasEpsilon = True
        while j < firstSets.length() and hasEpsilon:
            k = firstSets[j].length() - 1
            hasEpsilon = False
            while k > 1 and (not hasEpsilon):
                if firstSets[j][k].type == "EPSILON":
                    hasEpsilon = True
                k += 1
            if hasEpsilon:
                ir[i].next = make_rhs union A
                # union of all 
                # set next to rhs Union follow of A
            else:
                ir[i].next = make_rhs remove epsilon
                # set next to rhs sub epsilon
            j += 1
"""
            #add every first(B,i) to dict
            #if hasEpsilon, add follow(A) to dict
            #else remove epsilon from dict

    #for all productions
    #for each result bi
    # if every first(bi) contains epsilon then stuff remove epsilon
    # else
def print_tables(tables):
   print("Print tables in human-readable format")

def print_yaml(tables):
    print("Print tables in yaml format, or error if the involution of the next table fails")
   
