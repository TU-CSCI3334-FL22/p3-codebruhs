from lib2to3.pgen2 import token
from queue import Empty
from lib2to3.pgen2.grammar import Grammar

from mbnfScanner import Token


class Grammar:
    productions = [] # The Production is the thing that derives
    nonterminals = [] # The Non-terminal calls productions
    terminals = [] # The terminals simply are

    def __init__(self) -> None:
        pass
    
    def printIt(self) -> None:
        print('Grammar: ')
        i = '{'
        for production in self.productions:
            i += production[0]
            i += ', ['
            for terminal in production[1]:
                i += terminal + ', '
            i += '] '
            i += str(production[2])
            i+= '} '
            print(i)
            i = ''
        print(self.nonterminals)
        print(self.terminals)

grammar = Grammar()
def parseGrammar(tokensList):
    ProductionList(tokensList)
    terminalList = grammar.terminals
    toRemove = []
    for terminal in terminalList:
        if (isProduction(terminal)):
            Add(terminal, grammar.nonterminals)
            Add(terminal, toRemove)
    for item in toRemove:
        grammar.terminals.remove(item)
    return grammar

def ProductionList(tokensList):
    prodList = []
    index = 1
    while (tokensList):
        head = ProductionSet(tokensList, index)
        while (tokensList[0].type == "ALSODERIVES"):
            index += 1
            prodSet = ProductionSetPrime(tokensList, head, index)
            prodList.append(prodSet)
        if (tokensList[0].type != "SEMICOLON"):
            print(tokensList[0].lexeme)
            Die('not semicolon')
        tokensList.remove(tokensList[0])
        index += 1

def ProductionSet(tokensList, index):
    token = tokensList[0]
    head = token
    if (token.type != "SYMBOL") :
        print(token.lexeme)
        Die('not symbol')
    tokensList.remove(tokensList[0])

    if (tokensList[0].type != "DERIVES"):
        Die('not derives')
    tokensList.remove(tokensList[0])
    rightHandSide = RightHandSide(tokensList)
    Add((head.lexeme, rightHandSide, index), grammar.productions)
    return head

def ProductionSetPrime(tokensList, head, index):
    if (tokensList[0].type != "ALSODERIVES"):
        Die('not alsoderives')
    tokensList.remove(tokensList[0])
    rightHandSide = RightHandSide(tokensList)
    Add((head.lexeme, rightHandSide, index), grammar.productions)

def RightHandSide(tokensList):
    rightHandList = []
    while (tokensList[0].type == "SYMBOL"):
        rightHandList.append(tokensList[0].lexeme)
        if (isProduction(tokensList[0])):
            Add(tokensList[0].lexeme, grammar.nonterminals)
        else:
            Add(tokensList[0].lexeme, grammar.terminals)
        tokensList.remove(tokensList[0]); 
    if (tokensList[0].type == "EPSILON"):
        tokensList.remove(tokensList[0]); 
    return rightHandList

def isProduction(token):
    for production in grammar.productions:
        if (type(token) is Token):
            if (token.lexeme == production[0]):
                return True
        else:
            if (token == production[0]):
                return True
    return False

def Add(term, list):
    alreadyHere = False
    for item in list:
        if (term == item):
            alreadyHere = True
    if (not alreadyHere):
        list.append(term)

def Die(place):
    print('Comitting Die')
    print(place)
    quit()
