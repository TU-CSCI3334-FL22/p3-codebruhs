import getopt, sys
from llGrammars import *


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "htrw", ["help", "table", "revise", "worklist"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    printHelp = False
    printTable = False
    revise = False
    worklist = False
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-t", "--table"):
            printTable = True
        elif o in ("-r", "--revise"):
            revise = True
        elif o in ("-w", "--worklist"):
            worklist= True
        else:
            assert False, "unhandled option"
    if len(args) < 1:
        sys.exit("Please provide an input grammar")
    with open(args[0]) as f:
        contents = f.read()
        tokens = grammar_scan(contents)
        ir = grammar_parse(tokens)
        if revise:
            ir = fixLL(ir)
        tables = make_tables(ir, worklist)
        if printTable:
            print_yaml(tables)
        else:
            print_tables(tables)

if __name__ == "__main__":
    main()
  
