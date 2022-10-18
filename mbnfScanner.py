def main():
    file1 = open('grammars/CEG-RR', 'r')
    Lines = file1.readlines()

    dict = {}
    print("running")

    for line in Lines:
        #print(line)
        if line[0] == "/":
            continue
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
    
    print("Hello World")
    print(dict)

if __name__=="__main__":
    main()