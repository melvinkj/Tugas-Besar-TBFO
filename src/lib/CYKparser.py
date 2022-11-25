# Function to perform the CYK Algorithm
def cykParse(tokenText, CNFrules):
    token = tokenText.split(" ")
    n = len(token)
    print(token)
    
    # Initialize the table
    T = [[set([]) for j in range(n)] for i in range(n)]

    # Filling in the table
    for j in range(0, n):
        # Iterate over the rules
        for lhs, rule in CNFrules.items():
            for rhs in rule:
                # If a terminal is found
                if len(rhs) == 1 and rhs[0] == token[j]:
                    T[j][j].add(lhs)

        for i in range(j, -1, -1):  
            # Iterate over the range i to j + 1  
            for k in range(i, j):    
                # Iterate over the rules
                for lhs, rule in CNFrules.items():
                    for rhs in rule:  
                        # If a terminal is found
                        if len(rhs) == 2 and rhs[0] in T[i][k] and rhs[1] in T[k + 1][j]:
                            T[i][j].add(lhs)

    print(T[0][n-1])
    # If the token text is included in CNF rules, then the program is accepted
    if 'S' in (T[0][n-1]):
        print("Accepted")
    else:
        print("Syntax Error")