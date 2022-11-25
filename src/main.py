import argparse
import os
import sys
import re
from lib.tokenizer import createToken
from lib.CFGtoCNF import readGrammarFile, convertGrammar, mapGrammar
from lib.CYKparser import cykParse

def splash_screen():
    print()
    print("    888                              e88'Y88                                ,e, 888                ")
    print("    888  ,\"Y88b Y8b Y888P  ,\"Y88b   d888  'Y  e88 88e  888 888 8e  888 88e   \"  888  ,e e,  888,8, ")
    print("    888 \"8\" 888  Y8b Y8P  \"8\" 888  C8888     d888 888b 888 888 88b 888 888b 888 888 d88 88b 888 \"  ")
    print(" e  88P ,ee 888   Y8b \"   ,ee 888   Y888  ,d Y888 888P 888 888 888 888 888P 888 888 888   , 888    ")
    print("\"8\",P'  \"88 888    Y8P    \"88 888    \"88,d88  \"88 88\"  888 888 888 888 88\"  888 888  \"YeeP\" 888    ")
    print("                                                                   888                             ")
    print("                                                                   888                             ")
        

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

    # if not os.path.isfile(input_file):
    #     print("The file doesn't exist.")
    #     sys.exit()

    splash_screen()
    print("Processing...")
    print("Analyzing your file...")
    print("File name: " + str(input_file))


    # print('\n'.join(os.listdir(input_file)))

    token = createToken(str(input_file))
    token = [x.lower() for x in token]
    CNFgrammar = mapGrammar(convertGrammar((readGrammarFile("lib/grammar/cfg.txt"))))
    cykParse(token, CNFgrammar)


if __name__ == "__main__":
    main()