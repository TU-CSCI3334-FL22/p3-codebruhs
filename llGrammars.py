from makeTables import *

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
        # Each Table is a Dictionary, of Tokens mapped to Sets of Tokens
        tables.firstTable = makeFirst(ir)
        tables.followTable = makeFollow(ir, tables.firstTable)
        return(tables)

def print_tables(tables):
    print("Print tables in human-readable format")
    print("First Table:")
    print("----------------------")
    for i in tables.firstTable:
        print(i.lexeme + "\t | ", end="")
        for j in tables.firstTable[i]:
            print(j.lexeme + " ", end="")
        print("---------------------")
    print()

    print("Follow Table:")
    print("----------------------")
    for i in tables.followTable:
        print(i.lexeme + "\t | ", end="")
        for j in tables.firstTable[i]:
            print(j.lexeme + " ", end="")
        print("---------------------")
    print("\n")

    # Print Next Table - do later

def print_yaml(tables):
    print("Print tables in yaml format, or error if the involution of the next table fails")
   
