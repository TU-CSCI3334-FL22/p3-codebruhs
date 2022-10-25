
class Token:
    type = ""
    lexeme = ""

    
    def print(self) -> None:
        #printf('<%d, %d>' % (self.type, self.lexeme))
        print(self.type)
        print(self.lexeme)

def scan_grammar(contents):
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

    return scanned