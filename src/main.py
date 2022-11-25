import argparse
import os
import sys
import re
from lib.tokenizer import createToken
from lib.CFGtoCNF import readGrammarFile, convertGrammar, mapGrammar
from lib.CYKparser import cykParse



def main():
    program_parser = argparse.ArgumentParser(description='Accept or reject javascript syntax.')
    # Add the arguments
    program_parser.add_argument('File',
                        metavar='file',
                        type=argparse.FileType('r'),
                        help='enter .js file that you want to check')

    # Execute the parse_args() method
    args = program_parser.parse_args()

    input_file = args.File

    if not os.path.isfile(input_file):
        print("The file doesn't exist.")
        sys.exit()

    # print('\n'.join(os.listdir(input_file)))

    token = createToken(input_file)
    token = [x.lower() for x in token]
    CNFgrammar = mapGrammar(convertGrammar((readGrammarFile("lib/grammar/cfg.txt"))))
    cykParse(token, CNFgrammar)


if __name__ == "__main__":
    main()