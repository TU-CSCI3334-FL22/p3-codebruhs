class Token:
    type = ""

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
    return [Token()]

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
   
