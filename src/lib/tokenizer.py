import sys
import re
import fa
import os

# Token dari syntax ke token
tokenExprs = [
    (r'[ \t]+',                 None),
    (r'[/*][^\n]*[*/]',                None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),

    # Integer and String
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),
    (r'[\+\-]?[0-9]*\.[0-9]+',  "INT"),
    (r'[\+\-]?[1-9][0-9]+',     "INT"),
    (r'[\+\-]?[0-9]',           "INT"),
    (r'[\+\-]?[0-9]*\.[0-9]+[e][\+\-]?[0-9]+',  "INT"),
    (r'[\+\-]?[1-9][0-9]+[e][\+\-]?[0-9]+',     "INT"),
    (r'[\+\-]?[0-9][e][\+\-]?[0-9]+',           "INT"),

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
    (r'\/\/=',                  "FLOORDIVAS"),
    (r'\/\/',                   "FLOORDIV"),
    (r'\*=',                    "MULAS"),
    (r'/=',                     "DIVAS"),
    (r'\+=',                    "SUMAS"),
    (r'-=',                     "SUBAS"),
    (r'%=',                     "MODAS"),
    (r'\->',                    "ARROW"),
    (r'\+',                     "ADD"),
    (r'\-',                     "SUB"),
    (r'\*',                     "MUL"),
    (r'/',                      "DIV"),
    (r'%',                      "MOD"),
    (r'<=',                     "LEQ"),
    (r'<',                      "L"),
    (r'>=',                     "GEQ"),
    (r'>',                      "G"),
    (r'!=',                     "NEQ"),
    (r'\==',                    "ISEQ"),
    (r'\===',                   "ISEQEQ"),
    (r'\=(?!\=)',               "EQ"),
    (r'&&',                     "AND"),
    (r'\|\|',                   "OR"),
    (r'\?',                     "QMARK"),
    (r'\!',                     "NOT"),

    # Keyword
    (r'\blet\b',                "LET"),
    (r'\bvar\b',                "VAR"),
    (r'\bconst\b',              "CONST"),
    (r'\bif\b',                 "IF"),
    (r'\bthen\b',               "THEN"),
    (r'\belse\b',               "ELSE"),
    (r'\belse if\b',            "ELIF"),
    (r'\bswitch\b',             "SWITCH"),
    (r'\bcase\b',               "CASE"),
    (r'\bfor\b',                "FOR"),
    (r'\bwhile\b',              "WHILE"),
    (r'\bbreak\b',              "BREAK"),
    (r'\bcontinue\b',           "CONTINUE"),
    (r'\bfalse\b',              "FALSE"),
    (r'\btrue\b',               "TRUE"),
    (r'\bnull\b',               "NULL"),
    # CEKK ADA ATAU GAA
    (r'\bin\b',                 "IN"),
    (r'\bis\b',                 "IS"),
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
    currPos = 1         
    currLine = 1

    # Token result
    tokens = []

    while (currCol < len(text)):
        if (text[currCol] == "\n"):
            currLine += 1
            currPos += 1

        flag = None
        for tokenExpr in tokenExprs:
            pattern, tag = tokenExpr
            flag = re.compile(pattern).match(text, currCol)
            if flag:
                if tag:
                    token = tag
                    tokens.append(token)
                break

        if not flag:
            if (fa.isVariable(text[currCol])):
                token = "ID"
                tokens.append(token)
            else:
                print(f"\nSyntax error\nTerdapat karakter tidak valid {text[currCol]} pada baris {currLine}")
                sys.exit(1)
        else:
            currCol = flag.end(0)
        currPos += 1

    return tokens

def createToken(fileName):
    # Open and read file
    file = open(fileName, encoding="utf8")
    text = file.read()
    tokens = tokenize(text, tokenExprs)
    tokenResult = []
    file.close()

    for token in tokens:
        tokenResult.append(token)

    # # Write file testing
    # path = os.getcwd()
    # fileWrite = open(path + "/result/tokenResult.txt", 'w')
    # for token in tokenResult:
    #     fileWrite.write(str(token)+" ")
    #     # print(token)
    # fileWrite.close()

    return tokenResult

# if __name__ == "__main__": 
#     path = os.getcwd()
#     createToken(path + "/test/inputAcc.txt")