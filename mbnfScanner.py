def main():
    file1 = open('grammars\CEG-RR', 'r')
    Lines = file1.readlines()

    dict = {}
    printf("running")

    for line in Lines:
        if line[0] == "/":
            break
        words = line.split()
        for word in words:
            if word == ";":
                dict[";"] = "SEMICOLON"
            elif word == ":":
                dict[":"] = "DERIVES"
            elif word == "|":
                dict["|"] = "ALSODERIVES"
            elif word == "Epsilon" or word == "epsilon" or word == "EPSILON":
                dict["Epsilon"] = "EPSILON"
                dict["epsilon"] = "EPSILON"
                dict["EPSILON"] = "EPSILON"
            else:
                dict[word] = "SYMBOL"
    
    printf("Hello World")
    printf(dict)

