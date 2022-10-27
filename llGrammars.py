from makeTables import *
from mbnfParser import *
from mbnfScanner import *

class Tables:
    firstTable = {}
    followTable = {}
    nextTable = {}

def grammar_scan(contents):
    print("Scan contents into a list of tokens return it \n")
    scanned = scan_grammar(contents)
    #print(dict)
    #for token in scanned:
    #    print(token.type+", "+token.lexeme)
    return scanned

def grammar_parse(tokens):
    print("Read tokens into a grammar \n")
    parsedGrammar = parseGrammar(tokens)
    parsedGrammar.printIt()
    return parsedGrammar

def fixLL(ir):
    return ir

def make_tables(ir, worklist):
    tables = Tables()
    if(worklist):
        sys.exit("Worklists not supported yet!")
    else:
        print("Make and return the appropriate tables \n")
        # Each Table is a Dictionary, of Tokens mapped to Sets of Tokens
        tables.firstTable = makeFirst(ir)
        print(tables.firstTable)
        print('')
        tables.followTable = makeFollow(ir, tables.firstTable)
        print(tables.followTable)
        print('')
        tables.nextTable = makeNext(ir, tables.firstTable, tables.followTable)
        return(tables)

def print_tables(tables):
    print("\nPrint tables in human-readable format")
    print("First Table:")
    print("----------------------")
    for i in tables.firstTable:
        print(i + "\t | ", end="")
        for j in tables.firstTable[i]:
            print(j + " ", end="")
        print("")
    print()

    print("Follow Table:")
    print("----------------------")
    for i in tables.followTable:
        print(i + "\t | ", end="")
        for j in tables.followTable[i]:
            print(j + " ", end="")
        print("")
    print("\n")

    # Print Next Table - do later
    print("Next Table:")
    print("----------------------")
    for i in tables.nextTable:
        print(i[0] + "\t | ", end="")
        for j in i[1]:
            print(str(j) + " ", end="")
        print("")
    print("\n")

def print_yaml(tables):
    print("Print tables in yaml format, or error if the involution of the next table fails")
   
