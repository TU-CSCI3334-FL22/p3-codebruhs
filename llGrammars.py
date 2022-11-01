from makeTables import *
from mbnfParser import *
from mbnfScanner import *
from fixLL import rmDirLeftRecursion

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
    print()
    print("Fixing Left Recursion:")
    print("Old IR = ", end="")
    ir.printIt()
    newIr = rmDirLeftRecursion(ir)
    print("New IR = ", end="")
    newIr.printIt()
    return newIr

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
        print(tables.nextTable)
        return(tables)

def print_tables(tables):
    print("\nPrint tables in human-readable format")
    print("First Table:")
    print("-------------- --------")
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

    print("Next Table:")
    print("----------------------")
    for (index, i) in tables.nextTable:
        print(index, end="")
        print(". " + i + "\t | ", end="")
        for j in tables.nextTable[(index, i)]:
            print(j + " ", end="")
        print("")
    print("\n")

def print_yaml(tables,grammar):
    print("terminals: [",end="")
    i = len(grammar.terminals)
    for t in grammar.terminals:
        print(t, end="")
        if i>1:
            print(",",end=" ")
        i-=1
    print("]")
    print("non-terminals: [",end="")
    i = len(grammar.nonterminals)
    for nt in grammar.nonterminals:
        print(nt,end="")
        if i>1:
            print(",",end=" ")
        i-=1
    print("]")
    print("eof-marker: <EOF>\nerror-marker: --")
    print("start-symbol: ", end="")
    #fix
    nextTableList = list(tables.nextTable)
    start = nextTableList[0][1]
    print(start)
    print("productions: ")
    n=1
    for p in grammar.productions:
        print(" ",end="")
        print(n,end="")
        print(": {",end="")
        print(p[0],end="")
        print(": [",end="")
        start = True
        for prod in p[1]:
            if not start:
                print(", ",end="")
            print(prod,end="")
            start = False
        print("]}")            
        n+=1
    print("table:")
    #call next table:
    nxtTable = convertNextTable(tables,grammar)
    i=0
    for ntRow in nxtTable:
        print(" ",end="")
        print(grammar.nonterminals[i],end="")
        print(": {",end = "")
        j=0
        start = True
        for tCol in nxtTable[i]:
            if not tCol == -1:
                if  j > 0 and not start:
                    print(", ",end="")
                if j < len(grammar.terminals):
                    print(grammar.terminals[j],end = "")
                elif j < (len(grammar.terminals)+1):
                    print("EPSILON",end = "")
                elif j < (len(grammar.terminals) + 2):
                    print("EOF",end = "")
                print(": ",end = "")
                print(tCol,end = "")
                start = False
            j += 1
        i += 1
        print("}")
def convertNextTable(tables,grammar):
    involuted = [[-1 for c in range(len(grammar.terminals) + 2)] for r in range(len(grammar.nonterminals))]
    #[PLUS, MINUS, TIMES, DIV, LP, RP, NUMBER, IDENTIFIER],EPSILON,EOF   
    nonterminalInNextTable = {}
    terminalInNextTable = {}
    ind = 0
    for nonterm in grammar.nonterminals:
        nonterminalInNextTable[nonterm]=ind
        ind += 1

    ind = 0
    for term in grammar.terminals:
        terminalInNextTable[term]=ind
        ind += 1
    terminalInNextTable["EPSILON"]=ind
    terminalInNextTable["EOF"]=ind+1

    for (index, i) in tables.nextTable:
        #print(i + ": {", end="")
        for j in tables.nextTable[(index, i)]:
            #print(i)
            involuted[nonterminalInNextTable.get(i)][terminalInNextTable.get(j)]=index
    return involuted

   
