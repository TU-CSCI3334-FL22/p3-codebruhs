from lib2to3.pgen2 import token
from queue import Empty

class tokensList:
    type = []

def parseGrammar(tokensList):
    return ProductionList(tokensList)

def ProductionList(tokensList):
    prodList = []
    while (not tokensList.Empty):
        prodSet = ProductionSet(tokensList)
        prodList.append(prodSet)
        while (tokensList[0].type == "ALSODERIVES"):
            head = prodSet[0]
            prodSet = ProductionSetPrime(tokensList, head)
            prodList.append(prodSet)
        if (tokensList[0].type != "SEMICOLON"):
            Die()
    return prodList

def ProductionSet(tokensList):
    token = tokensList[0]
    head = token
    if (token.type != "SYMBOL") :
        Die()
    tokensList.remove(tokensList[0])
    if (tokensList[0] != "DERIVES"):
        Die()
    tokensList.remove(tokensList[0])
    rightHandSide = RightHandSide(tokensList)
    return tuple(head, rightHandSide)

def ProductionSetPrime(tokensList, head):
    if (tokensList[0] != "ALSODERIVES"):
        Die()
    tokensList.remove(tokensList[0])
    rightHandSide = RightHandSide(tokensList)
    return tuple(head, rightHandSide)

def RightHandSide(tokensList):
    rightHandList = []
    while (tokensList[0].type == "SYMBOL"):
        rightHandList.append(tokensList[0])
        tokensList.remove(tokensList[0]); 
    return rightHandList

def Die():
    exit(0)
