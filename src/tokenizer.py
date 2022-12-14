import sys
import re
from . import fa
import os

# Token dari syntax ke token
tokenExprs = [
    (r'[ \t]+',                 None),
    (r'\/\/[^\n]*',                None),
    (r'[\n]+[ \t]*\/\*[(?!(\/\*))\w\W]*\*\\',  None),

    # String
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),

    # Delimiter
    (r'\n',                     "NEWLINE"),
    (r'\;\n',                   "NEWLINE"),
    (r'\(',                     "KBKI"), # Kurung Biasa KIri
    (r'\)',                     "KBKA"),
    (r'\[',                     "KSKI"), # Kurung Siku KIri
    (r'\]',                     "KSKA"),
    (r'\{',                     "KKKI"), # Kurung Kurawal Kiri
    (r'\}',                     "KKKA"),
    (r'\;',                     "TITIKKOMA"), 
    (r'\:',                     "TITIKDUA"),

    # Operator
    (r'\*\*=',                  "POWAS"),
    (r'\*\*',                   "POW"),
    (r'\*=',                    "MULAS"),
    (r'/=',                     "DIVAS"),
    (r'\+=',                    "SUMAS"),
    (r'-=',                     "SUBAS"),
    (r'%=',                     "MODAS"),
    (r'\->',                    "ARROW"),
    (r'\+(?!\+)',               "ADD"),
    (r'\-(?!\-)',               "SUB"),
    (r'\*',                     "MUL"),
    (r'/',                      "DIV"),
    (r'%',                      "MOD"),
    (r'<=',                     "LEQ"),
    (r'<',                      "L"),
    (r'>=',                     "GEQ"),
    (r'>',                      "G"),
    (r'!=',                     "NEQ"),
    (r'!==',                     "NEQEQ"),
    (r'\==(?!\=)',              "ISEQ"),
    (r'\===',                   "ISEQEQ"),
    (r'\=(?!\=)',               "EQ"),
    (r'&=',                     "ANDAS"),
    (r'\|=',                    "ORAS"),
    (r'&(?!&)',                 "AND"),
    (r'\|(?!\|)',               "OR"),
    (r'\?(?!\?)',               "QMARK"),
    (r'\!',                      "NOT"),
    (r'<<=',                     "LSHIFTAS"),
    (r'>>=',                     "RSHIFTAS"),
    (r'>>>=',                     "URSHIFT"),
    (r'\^=',                     "XORAS"),
    (r'&&=',                     "ANDLOGAS"),
    (r'\|\|=',                     "ORLOGAS"),
    (r'\?\?=',                     "NULLISHAS"),
    (r'<<',                     "LSHIFT"),
    (r'>>(?!>)',                     "RSHIFT"),
    (r'>>>',                     "URSHIFT"),
    (r'\^',                     "XOR"),
    (r'&&',                     "ANDLOG"),
    (r'\|\|',                     "ORLOG"),
    (r'\?\?',                     "NULLISH"),
    (r'\+\+',                     "INC_OP"),
    (r'\-\-',                     "DEC_OP"),

    # Integer
    (r'[\+\-]?[0-9]*\.[0-9]+',  "INT"),
    (r'[\+\-]?[1-9][0-9]+',     "INT"),
    (r'[\+\-]?[0-9]',           "INT"),
    (r'[\+\-]?[0-9]*\.[0-9]+[e][\+\-]?[0-9]+',  "INT"),
    (r'[\+\-]?[1-9][0-9]+[e][\+\-]?[0-9]+',     "INT"),
    (r'[\+\-]?[0-9][e][\+\-]?[0-9]+',           "INT"),

    # Keyword
    (r'\blet\b',                "LET"),
    (r'\bvar\b',                "VAR"),
    (r'\bconst\b',              "CONST"),
    (r'\belse if\b',            "ELIF"),
    (r'\bif\b',                 "IF"),
    (r'\belse\b',               "ELSE"),
    (r'\bswitch\b',             "SWITCH"),
    (r'\bcase\b',               "CASE"),
    (r'\bfor\b',                "FOR"),
    (r'\bwhile\b',              "WHILE"),
    (r'\bbreak\b',              "BREAK"),
    (r'\bcontinue\b',           "CONTINUE"),
    (r'\bdefault\b',            "DEFAULT"),
    (r'\bfalse\b',              "FALSE"),
    (r'\btrue\b',               "TRUE"),
    (r'\bnull\b',               "NULL"),
    (r'\bin\b',                 "IN"),
    (r'\bfunction\b',           "FUNC_STR"),
    (r'\breturn\b',             "RETURN"),
    (r'\btry\b',                "TRY"),
    (r'\bcatch\b',              "CATCH"),
    (r'\bfinally\b',            "FINALLY"),
    (r'\bthrow\b',              "THROW"),
    (r'\bdelete\b',             "DELETE"),
    (r'\,',                     "COMMA"),
    (r'\w+[.]\w+',              "KARTITIK"),
    (r'\.',                     "TITIK"),
    (r'\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',       "MULTILINE"),
    (r'\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',       "MULTILINE"),

    # Variable 
    # (r'[A-Za-z_][A-Za-z0-9_]*', "ID"),
]

# Melakukan tokenize pada text sesuai dengan token expression
def tokenize(text, tokenExprs):
    # Current column, position, and line
    currCol = 0         
    currPos = 0         
    currLine = 1

    # Token result
    tokens = []

    while (currCol < len(text)):
        if (text[currCol] == "\n"):
            currLine += 1
            currPos = 1

        isMatch = None

        for tokenExpr in tokenExprs:
            pattern, tag = tokenExpr
            regex = re.compile(pattern)
            isMatch = regex.match(text, currCol)
            if isMatch:
                if tag:
                    token = tag
                    tokens.append(token)
                break

        if not isMatch:
            isVar = fa.isVariable(text[currCol])
            if (isVar):
                pattern, tag = (r'[A-Za-z_$][A-Za-z0-9_$]*', "ID")
                regex = re.compile(pattern)
                isMatch = regex.match(text, currCol)
                token = tag
                tokens.append(token)
                currCol = isMatch.end(0)
            else:
                print(f"\n\033[91mSyntax error\033[0m\nTerdapat karakter tidak valid \033[91m{text[currCol]}\033[0m pada baris {currLine}")
                sys.exit(1)
        else:
            currCol = isMatch.end(0)
        currPos += 1

    return tokens

def createToken(fileName):
    # Open and read file
    file = open(fileName, encoding="utf8")
    text = file.read()
    file.close()

    tokens = tokenize(text, tokenExprs)
    tokenResult = []


    for token in tokens:
        tokenResult.append(token)

    # # Write file testing
    # path = os.getcwd()
    # fileWrite = open(path + "/result/tokenResult.txt", 'w')
    # for token in tokenResult:
    #     fileWrite.write(str(token)+" ")
    #     # print(token)
    # fileWrite.close()

    return " ".join(tokenResult)

# if __name__ == "__main__": 
#     path = os.getcwd()
#     createToken(path + "/test/inputAcc.txt")