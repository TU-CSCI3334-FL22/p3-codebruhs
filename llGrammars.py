
from mbnfParser import *
from mbnfScanner import *

class Tables:
    firstTable = {}
    followTable = {}
    nextTable = {}

def grammar_scan(contents):
    print("Scan contents into a list of tokens return it")

    scanned = scan_grammar(contents)
    #print("Hello World")
    #print(dict)
    #for token in scanned:
    #    print(token.type+", "+token.lexeme)
    return scanned

def grammar_parse(tokens):
    print("Read tokens into a grammar")
    parsedGrammar = parseGrammar(tokens)
    parsedGrammar.print()
    return parsedGrammar

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
   
