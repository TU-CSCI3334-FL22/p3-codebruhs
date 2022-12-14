
class Token:
    type = ""
    lexeme = ""

    def prettyPrint(self) -> None:
        return ('<'+self.type+","+self.lexeme+">")

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
