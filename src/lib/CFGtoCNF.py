import os

def is_terminal(string):
    list_of_terminal = [
        "EQ",
        "ISEQ",
        "KBKI",
        "KBKA",
        "TITIKKOMA",
        "TITIKDUA",
        "ADD",
        "SUB",
        "MUL",
        "DIV",
        "MOD",
        "POW",
        "FLOORDIV",
        "LEQ",
        "LET",
        "L",
        "GEQ",
        "G",
        "NEQ",
        "SUBAS",
        "MULAS",
        "SUMAS",
        "DIVAS",
        "MODAS",
        "POWAS",
        "FLOORDIVAS",
        "AND",
        "OR",
        "NOT",
        "IF",
        "THEN",
        "ELSE",
        "ELIF",
        "WHILE",
        "RANGE",
        "FALSE",
        "TRUE",
        "NONE",
        "BREAK",
        "AS",
        "CLASS",
        "CONTINUE",
        "DEF",
        "FOR",
        "FROM",
        "FORMAT",
        "IMPORT",
        "IN",
        "IS",
        "RETURN",
        "RAISE",
        "PASS",
        "WITH",
        "COMMA",
        "KARTITIK",
        "TITIK",
        "PETIKSATU",
        "PETIKDUA",
        "KSKI",
        "KSKA",
        "KKKI",
        "KKKA",
        "INT",
        "STRING",
        "MULTILINE",
        "ID",
        "NEWLINE",
        "TYPE",
        "ARROW"
    ]
    
    return string in list_of_terminal

def is_variables(string):
    return not is_terminal(string)

# terminal = keyword.kwlist
# dictRule = {}
# #Read CFG txt
# def readGrammarFile(file):
#     dir =os.path.join(os.path.dirname(os.path.realpath(__file__)),  file)
#     with open(dir) as cfg_file:
#         row = cfg_file.readlines()
#         rowConverted = []
#         for i in range(len(row)):
#             splitRow = row[i].replace("->", "").split()
#             rowConverted.append(splitRow)
#     return rowConverted

# # Adding rule to global var
# def addGrammarRule(rule):
#     global dictRule
#     if rule[0] not in dictRule:
#         dictRule[rule[0]] = []
#     dictRule[rule[0]].append(rule[1:])

# def convertGrammar(grammar):
#     global dictRule
#     idx = 0
#     unitProductions, res = [], []
#     for rule in grammar:
#         new_rules = []
#       # buat yang cuma satu nonterminal/terminal di kanan
#         if len(rule) == 2 and not rule[1][0].islower() :
#             unitProductions.append(rule)
#             addGrammarRule(rule)
#             continue
#       # Proses if lebih dari 3 nonterminalnya ini bakal di split jadi cuma 3 doang  
#         while len(rule) > 3: 
#             new_rules.append([f"{rule[0]}{idx}", rule[1], rule[2]])
#             rule = [rule[0]] + [f"{rule[0]}{idx}"] + rule[3:]
#             idx += 1
#         if rule:
#             addGrammarRule(rule)
#             res.append(rule)
#         if new_rules:
#             for i in range(len(new_rules)):
#                 res.append(new_rules[i])

#     # Proses cuma yang ada 1 non terminal di kanan
#     while unitProductions:
#         rule = unitProductions.pop() 
#         if rule[1] in dictRule:
#             for item in dictRule[rule[1]]:
#                 new_rule = [rule[0]] + item
#           # nonterminal dikanan bakal dirubah either kalo panjangnya 3 / ada terminal
#             if len(new_rule) > 2 or new_rule[1][0].islower():
#                 res.append(new_rule)
#           #Kalo cuma 2 tp dia bukan terminal masukin lg ke production ujungnya bakal dirubah jadi terminal
#             else:
#                 unitProductions.append(new_rule)
#             addGrammarRule(new_rule)
#     return res

# def mapGrammar(grammar):
#     map = {}
#     for rule in grammar :
#         map[str(rule[0])] = []
#     for rule in grammar :
#         elm = []
#         for idxRule in range(1, len(rule)) :
#             apd = rule[idxRule]
#             elm.append(apd)
#         map[str(rule[0])].append(elm)
#     return map

# def writeGrammar(grammar):
#     dir =os.path.join(os.path.dirname(os.path.realpath(__file__)),  'CNF.txt')
#     file = open(dir, 'w')
#     for rule in grammar:
#         file.write(rule[0])
#         file.write(" -> ")
#         for i in rule[1:]:
#             file.write(i)
#             file.write(" ")
#         file.write("\n")
#     file.close()

# #Print hasil files untuk debugging
# def printGrammar(grammar):
#     for grammarRule in grammar:
#         for i in range(len(grammarRule)):
#             if i != 0: 
#                 print(grammarRule[i], end=' ')
#             else: # print panah jika merupakan terminal awal
#                 print(grammarRule[i], " -> ", end='')        
#         print("\n")

def CFG_to_CNF(file):
    dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),  file) 
    file = open(dir, "r")
    CFG = {}

    baris = file.readline()
    while baris != "":
        head, body = baris.replace("\n", "").split(" -> ")
        
        if head not in CFG.keys():
            CFG[head] = [body.split(" ")]
        else:
            CFG[head].append(body.split(" "))

        baris = file.readline()

    file.close()

    # STEP 1: If the start symbol S occurs on some right side, create a new start symbol S' and a new production S' -> S.
    list_head = list(CFG.keys())
    list_body = list(CFG.values())
    start_symbol = list_head[0]
    add_new_rule = False

    for rules in list_body:
        for rule in rules:
            if start_symbol in rule:
                add_new_rule = True
                break
        if add_new_rule:
            break

    if add_new_rule:
        new_rule = {"START" : [[start_symbol]]}
        new_rule.update(CFG)
        CFG = new_rule

    # STEP 2: Remove unit productions.
    contain_unit = True

    while contain_unit:
        unit_productions = {}
        contain_unit = False
        
        for head, body in CFG.items():
            for rule in body:
                if len(rule) == 1 and is_variables(rule[0]):
                    contain_unit = True
                    if head not in unit_productions.keys():
                        unit_productions[head] = [[rule[0]]]
                    else:
                        unit_productions[head].append([rule[0]])

        for head_unit, body_unit in unit_productions.items():
            for rule_unit in body_unit:
                for head, body in CFG.items():
                    if len(rule_unit) == 1 and head == rule_unit[0]:
                        new_rule = {head_unit : body}
                        if head_unit not in CFG.keys():
                            CFG[head_unit] = body
                        else:
                            for rule in body:
                                if rule not in CFG[head_unit]:
                                    CFG[head_unit].append(rule)
    
        for head_unit, body_unit in unit_productions.items():
            for rule_unit in body_unit:
                if len(rule_unit) == 1:
                    CFG[head_unit].remove(rule_unit)

    # STEP 3: Replace Body with 3 or more Variables
    new_productions = {}
    del_productions = {}

    i = 0
    for head, body in CFG.items():
        for rule in body:
            head_symbol = head
            temp_rule = [r for r in rule]
            if len(temp_rule) > 2:
                while len(temp_rule) > 2:
                    new_symbol = f"X{i}"
                    if head_symbol not in new_productions.keys():
                        new_productions[head_symbol] = [[temp_rule[0], new_symbol]]
                    else:
                        new_productions[head_symbol].append([temp_rule[0], new_symbol])
                    head_symbol = new_symbol
                    temp_rule.remove(temp_rule[0])
                    i += 1
                else:
                    if head_symbol not in new_productions.keys():
                        new_productions[head_symbol] = [temp_rule]
                    else:
                        new_productions[head_symbol].append(temp_rule)
                    
                    if head not in del_productions.keys():
                        del_productions[head] = [rule]
                    else:
                        del_productions[head].append(rule)

    for new_head, new_body in new_productions.items():
        if new_head not in CFG.keys():
            CFG[new_head] = new_body
        else:
            CFG[new_head].extend(new_body)

    for del_head, del_body in del_productions.items():
        for del_rule in del_body:
            CFG[del_head].remove(del_rule)

    # STEP 4: Replace Terminal adjacent to a Variables
    new_productions = {}
    del_productions = {}

    j = 0
    k = 0
    for head, body in CFG.items():
        for rule in body:
            if len(rule) == 2 and is_terminal(rule[0]) and is_terminal(rule[1]):
                new_symbol_Y = f"Y{j}"
                new_symbol_Z = f"Z{k}"

                if head not in new_productions.keys():
                    new_productions[head] = [[new_symbol_Y, new_symbol_Z]]
                else:
                    new_productions[head].append([new_symbol_Y, new_symbol_Z])
                    
                new_productions[new_symbol_Y] = [[rule[0]]]
                new_productions[new_symbol_Z] = [[rule[1]]]

                if head not in del_productions.keys():
                    del_productions[head] = [rule]
                else:
                    del_productions[head].append(rule)

                j += 1
                k += 1

            elif len(rule) == 2 and is_terminal(rule[0]):
                new_symbol_Y = f"Y{j}"

                if head not in new_productions.keys():
                    new_productions[head] = [[new_symbol_Y, rule[1]]]
                else:
                    new_productions[head].append([new_symbol_Y, rule[1]])

                new_productions[new_symbol_Y] = [[rule[0]]]

                if head not in del_productions.keys():
                    del_productions[head] = [rule]
                else:
                    del_productions[head].append(rule)

                j += 1

            elif len(rule) == 2 and is_terminal(rule[1]):
                new_symbol_Z = f"Z{k}"

                if head not in new_productions.keys():
                    new_productions[head] = [[rule[0], new_symbol_Z]]
                else:
                    new_productions[head].append([rule[0], new_symbol_Z])

                new_productions[new_symbol_Z] = [[rule[1]]]

                if head not in del_productions.keys():
                    del_productions[head] = [rule]
                else:
                    del_productions[head].append(rule)

                k += 1

            else:
                pass

    for new_head, new_body in new_productions.items():
        if new_head not in CFG.keys():
            CFG[new_head] = new_body
        else:
            CFG[new_head].extend(new_body)

    for del_head, del_body in del_productions.items():
        for del_rule in del_body:
            CFG[del_head].remove(del_rule)

    return CFG

# if __name__ == "__main__":
    # writeGrammar(convertGrammar((readGrammarFile("CFG.txt")))) 
    # printGrammar(readGrammarFile("CFG.txt"))