'''
|1 | Grammar |$\rightarrow$| ProductionList |
|2 | ProductionList |$\rightarrow$|  ProductionSet SEMICOLON ProductionList|
|3 |                |$\mid$ | EPSILON|
|4 |ProductionSet |$\rightarrow$| SYMBOL DERIVES RightHandSide ProductionSet'|
|5 |ProductionSet' |$\rightarrow$| ALSODERIVES RightHandSide ProductionSet'|
|6 |              |$\mid$|EPSILON|
|7 | RightHandSide  |$\rightarrow$|SymbolList|
|8 |                 |$\mid$| EPSILON|
|9 | SymbolList     |$rightarrow$|SYMBOL SymbolList|
|10|                |$\mid$| EPSILON|
