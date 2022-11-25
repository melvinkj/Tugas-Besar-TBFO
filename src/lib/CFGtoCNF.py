import keyword
import os

terminal = keyword.kwlist
dictRule = {}
#Read CFG txt
def readGrammarFile(file):
    dir =os.path.join(os.path.dirname(os.path.realpath(__file__)),  file)
    with open(dir) as cfg_file:
        row = cfg_file.readlines()
        rowConverted = []
        for i in range(len(row)):
            splitRow = row[i].replace("->", "").split()
            rowConverted.append(splitRow)
    return rowConverted

# Adding rule to global var
def addGrammarRule(rule):
    global dictRule
    if rule[0] not in dictRule:
        dictRule[rule[0]] = []
    dictRule[rule[0]].append(rule[1:])

def convertGrammar(grammar):
    global dictRule
    idx = 0
    unitProductions, res = [], []
    for rule in grammar:
        new_rules = []
      # buat yang cuma satu nonterminal/terminal di kanan
        if len(rule) == 2 and not rule[1][0].islower() :
            unitProductions.append(rule)
            addGrammarRule(rule)
            continue
      # Proses if lebih dari 3 nonterminalnya ini bakal di split jadi cuma 3 doang  
        while len(rule) > 3: 
            new_rules.append([f"{rule[0]}{idx}", rule[1], rule[2]])
            rule = [rule[0]] + [f"{rule[0]}{idx}"] + rule[3:]
            idx += 1
        if rule:
            addGrammarRule(rule)
            res.append(rule)
        if new_rules:
            for i in range(len(new_rules)):
                res.append(new_rules[i])

    # Proses cuma yang ada 1 non terminal di kanan
    while unitProductions:
        rule = unitProductions.pop() 
        if rule[1] in dictRule:
            for item in dictRule[rule[1]]:
                new_rule = [rule[0]] + item
          # nonterminal dikanan bakal dirubah either kalo panjangnya 3 / ada terminal
            if len(new_rule) > 2 or new_rule[1][0].islower():
                res.append(new_rule)
          #Kalo cuma 2 tp dia bukan terminal masukin lg ke production ujungnya bakal dirubah jadi terminal
            else:
                unitProductions.append(new_rule)
            addGrammarRule(new_rule)
    return res

def mapGrammar(grammar):
    map = {}
    for rule in grammar :
        map[str(rule[0])] = []
    for rule in grammar :
        elm = []
        for idxRule in range(1, len(rule)) :
            apd = rule[idxRule]
            elm.append(apd)
        map[str(rule[0])].append(elm)
    return map

def writeGrammar(grammar):
    dir =os.path.join(os.path.dirname(os.path.realpath(__file__)),  'CNF.txt')
    file = open(dir, 'w')
    for rule in grammar:
        file.write(rule[0])
        file.write(" -> ")
        for i in rule[1:]:
            file.write(i)
            file.write(" ")
        file.write("\n")
    file.close()

#Print hasil files untuk debugging
def printGrammar(grammar):
    for grammarRule in grammar:
        for i in range(len(grammarRule)):
            if i != 0: 
                print(grammarRule[i], end=' ')
            else: # print panah jika merupakan terminal awal
                print(grammarRule[i], " -> ", end='')        
        print("\n")

if __name__ == "__main__":
    writeGrammar(convertGrammar((readGrammarFile("CFG.txt")))) 
    # printGrammar(readGrammarFile("CFG.txt"))