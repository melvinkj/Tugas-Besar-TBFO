import argparse
import os
import sys
import re
from lib.tokenizer import createToken
from lib.CFGtoCNF import CFG_to_CNF
from lib.CYKparser import cykParse
from termcolor import colored


def splash_screen():
    print(colored("    888                            dP\"8                 ,e,            d8    888 88e                                       ", "red"))
    print(colored("    888  ,\"Y88b Y8b Y888P  ,\"Y88b C8b Y  e88'888 888,8,  \"  888 88e   d88    888 888D  ,\"Y88b 888,8,  dP\"Y  ,e e,  888,8, ", "yellow"))
    print(colored("    888 \"8\" 888  Y8b Y8P  \"8\" 888  Y8b  d888  '8 888 \"  888 888 888b d88888  888 88\"  \"8\" 888 888 \"  C88b  d88 88b 888 \"  ", "green"))
    print(colored(" e  88P ,ee 888   Y8b \"   ,ee 888 b Y8D Y888   , 888    888 888 888P  888    888      ,ee 888 888     Y88D 888   , 888    ", "cyan"))
    print(colored("\"8\",P'  \"88 888    Y8P    \"88 888 8edP   \"88,e8' 888    888 888 88\"   888    888      \"88 888 888    d,dP   \"YeeP\" 888    ", "blue"))
    print(colored("                                                            888                                                           ", "magenta"))
    print(colored("                                                            888                                                             ", "magenta"))     

def main():
    program_parser = argparse.ArgumentParser(description='Accept or reject javascript syntax.')
    # Add the arguments
    program_parser.add_argument('File',
                        metavar='file',
                        type=argparse.FileType('r'),
                        help='enter .js file that you want to check')

    # Execute the parse_args() method
    args = program_parser.parse_args()

    input_file = args.File.name

    # if not os.path.isfile(input_file):
    #     print("The file doesn't exist.")
    #     sys.exit()

    print()
    splash_screen()
    print("Processing...")
    print("Analyzing your file...")
    print("File name: " + str(input_file))


    # print('\n'.join(os.listdir(input_file)))

    token = createToken(input_file)
    CNFgrammar = CFG_to_CNF("./CFG.txt")
    cykParse(token, CNFgrammar)


if __name__ == "__main__":
    main()