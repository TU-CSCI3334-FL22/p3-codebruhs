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

        
def print_tables(tables):
   print("Print tables in human-readable format")

def print_yaml(tables):
    print("Print tables in yaml format, or error if the involution of the next table fails")
   
