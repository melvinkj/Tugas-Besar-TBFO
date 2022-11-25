import os

def is_terminal(string):
    terminal_list = [
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
        "FALSE",
        "TRUE",
        "BREAK",
        "CONTINUE",
        "FOR",
        "IN",
        "RETURN",
        "COMMA",
        "KARTITIK",
        "TITIK",
        "KSKI",
        "KSKA",
        "KKKI",
        "KKKA",
        "INT",
        "STRING",
        "MULTILINE",
        "NEWLINE",
        "ARROW",
        "QMARK",
        "VAR",
        "ID",
        "CONST",
        "SWITCH",
        "CASE",
        "NULL",
        "FUNC_STR",
        "TRY",
        "CATCH",
        "FINALLY",
        "THROW",
        "DELETE",
        "ISEQEQ", 
        "ANDAS",
        "ORAS",
        "LSHIFTAS",
        "RSHIFTAS",
        "URSHIFT",
        "XORAS",
        "ANDLOGAS",
        "ORLOGAS",
        "NULLISHAS",
        "LSHIFT",
        "RSHIFT",
        "URSHIFT",
        "XOR",
        "ANDLOG",
        "ORLOG",
        "NULLISH",
        "INC_OP",
        "DEC_OP"
        "DEC_OP",
        "DEFAULT"
    ]
    
    return string in terminal_list

def is_variables(string):
    return not is_terminal(string)

def convertFileToDictionary(file):
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
    return CFG

def addingProduction(newProductions, delProductions, CFG):
    for new_head, new_body in newProductions.items():
        if new_head not in CFG.keys():
            CFG[new_head] = new_body
        else:
            CFG[new_head].extend(new_body)

    for del_head, del_body in delProductions.items():
        for del_rule in del_body:
            CFG[del_head].remove(del_rule)
    
    return CFG

def startProduction(CFG):
    list_head = list(CFG.keys())
    list_body = list(CFG.values())
    start = list_head[0]
    add_new = False

    for rules in list_body:
        for rule in rules:
            if start in rule:
                add_new = True
                break
        if add_new:
            break

    if add_new:
        new_rule = {"START" : [[start]]}
        new_rule.update(CFG)
        CFG = new_rule
    return CFG

def removeUnitProduction(CFG):
    contain = True
    while (contain):
        unit_productions = {}
        contain = False
        for head, body in CFG.items():
            for rule in body:
                if len(rule) == 1 and is_variables(rule[0]):
                    contain = True
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
    return CFG
def CFG_to_CNF(file):
    CFG = convertFileToDictionary(file)

    # Langkah Pertama: jika ada Start Symbol 'S' di bagian kanan panah, maka menambahkan production symbol baru yaitu S'
    CFG = startProduction(CFG)

    # Kedua: Remove unit productions pada grammar.
    CFG = removeUnitProduction(CFG)

    # Ketiga: Replace Body dengan 3 atau lebih variables
    first_newProductions = {}
    first_throwProductions = {}
    i = 0
    for head, body in CFG.items():
        for rule in body:
            head_symbol = head
            temp_rule = [r for r in rule]
            if len(temp_rule) > 2:
                while len(temp_rule) > 2:
                    new_symbol = f"X{i}"
                    if head_symbol not in first_newProductions.keys():
                        first_newProductions[head_symbol] = [[temp_rule[0], new_symbol]]
                    else:
                        first_newProductions[head_symbol].append([temp_rule[0], new_symbol])
                    head_symbol = new_symbol
                    temp_rule.remove(temp_rule[0])
                    i += 1
                else:
                    if head_symbol not in first_newProductions.keys():
                        first_newProductions[head_symbol] = [temp_rule]
                    else:
                        first_newProductions[head_symbol].append(temp_rule)
                    
                    if head not in first_throwProductions.keys():
                        first_throwProductions[head] = [rule]
                    else:
                        first_throwProductions[head].append(rule)

    CFG = addingProduction(first_newProductions, first_throwProductions, CFG)
    
    #Keempat: ganti Terminal berdekatan menjadi Variables
    final_newProductions = {}
    final_throwProductions = {}
    j = 0
    k = 0
    for head, body in CFG.items():
        for rule in body:
            if len(rule) == 2 and is_terminal(rule[0]) and is_terminal(rule[1]):
                new_symbol_Y = f"Y{j}"
                new_symbol_Z = f"Z{k}"

                if head not in final_newProductions.keys():
                    final_newProductions[head] = [[new_symbol_Y, new_symbol_Z]]
                else:
                    final_newProductions[head].append([new_symbol_Y, new_symbol_Z])
                    
                final_newProductions[new_symbol_Y] = [[rule[0]]]
                final_newProductions[new_symbol_Z] = [[rule[1]]]

                if head not in final_throwProductions.keys():
                    final_throwProductions[head] = [rule]
                else:
                    final_throwProductions[head].append(rule)
                j += 1
                k += 1

            elif len(rule) == 2 and is_terminal(rule[0]):
                new_symbol_Y = f"Y{j}"

                if head not in final_newProductions.keys():
                    final_newProductions[head] = [[new_symbol_Y, rule[1]]]
                else:
                    final_newProductions[head].append([new_symbol_Y, rule[1]])

                final_newProductions[new_symbol_Y] = [[rule[0]]]

                if head not in final_throwProductions.keys():
                    final_throwProductions[head] = [rule]
                else:
                    final_throwProductions[head].append(rule)
                j += 1

            elif len(rule) == 2 and is_terminal(rule[1]):
                new_symbol_Z = f"Z{k}"

                if head not in final_newProductions.keys():
                    final_newProductions[head] = [[rule[0], new_symbol_Z]]
                else:
                    final_newProductions[head].append([rule[0], new_symbol_Z])

                final_newProductions[new_symbol_Z] = [[rule[1]]]

                if head not in final_throwProductions.keys():
                    final_throwProductions[head] = [rule]
                else:
                    final_throwProductions[head].append(rule)
                k += 1
            else:
                pass

    CFG = addingProduction(final_newProductions, final_throwProductions, CFG)

    return CFG
