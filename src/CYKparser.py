# Function to perform the CYK Algorithm
def cykParse(tokenText, CNFrules):
    token = tokenText.split(" ")
    n = len(token)
    # print(token)
    
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

    # print(T[0][n-1])
    # If the token text is included in CNF rules, then the program is accepted
    if 'S' in (T[0][n-1]):
        print()
        print("\033[92m      .o.                                                    .                   .o8  \033[0m")
        print("\033[92m     .888.                                                 .o8                  \"888  \033[0m")
        print("\033[92m    .8\"888.      .ooooo.   .ooooo.   .ooooo.  oo.ooooo.  .o888oo  .ooooo.   .oooo888  \033[0m")
        print("\033[92m   .8' `888.    d88' `\"Y8 d88' `\"Y8 d88' `88b  888' `88b   888   d88' `88b d88' `888  \033[0m")
        print("\033[92m  .88ooo8888.   888       888       888ooo888  888   888   888   888ooo888 888   888  \033[0m")
        print("\033[92m .8'     `888.  888   .o8 888   .o8 888    .o  888   888   888 . 888    .o 888   888  \033[0m")
        print("\033[92mo88o     o8888o `Y8bod8P' `Y8bod8P' `Y8bod8P'  888bod8P'   \"888\" `Y8bod8P' `Y8bod88P\" \033[0m")
        print("\033[92m                                               888                                    \033[0m")
        print("\033[92m                                              o888o                                   \033[0m")
                                                                                      
    else:
        print()
        print("\033[91m .oooooo..o                             .                             oooooooooooo                                      \033[0m")
        print("\033[91md8P'    `Y8                           .o8                             `888'     `8                                      \033[0m")
        print("\033[91mY88bo.      oooo    ooo ooo. .oo.   .o888oo  .oooo.   oooo    ooo      888         oooo d8b oooo d8b  .ooooo.  oooo d8b \033[0m")
        print("\033[91m `\"Y8888o.   `88.  .8'  `888P\"Y88b    888   `P  )88b   `88b..8P'       888oooo8    `888\"\"8P `888\"\"8P d88' `88b `888\"\"8P \033[0m")
        print("\033[91m     `\"Y88b   `88..8'    888   888    888    .oP\"888     Y888'         888    \"     888      888     888   888  888     \033[0m")
        print("\033[91moo     .d8P    `888'     888   888    888 . d8(  888   .o8\"'88b        888       o  888      888     888   888  888     \033[0m")
        print("\033[91m8\"\"88888P'      .8'     o888o o888o   \"888\" `Y888\"\"8o o88'   888o     o888ooooood8 d888b    d888b    `Y8bod8P' d888b    \033[0m")
        print("\033[91m            .o..P'                                                                                                      \033[0m")
        print("\033[91m            `Y8P'                                                                                                       \033[0m")
                                                                                                                                