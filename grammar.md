'''
1. Grammar        -> ProductionList
2. ProductionList -> ProductionSet SEMICOLON ProductionList
3.                 | EPSILON
4. ProductionSet  -> SYMBOL DERIVES RightHandSide ProductionSet'
5. ProductionSet' -> ALSODERIVES RightHandSide ProductionSet'
6.                 | EPSILON
7. RightHandSide  -> SymbolList
8.                 | EPSILON
9. SymbolList     -> SYMBOL SymbolList
10.                | EPSILON
