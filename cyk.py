from parse import treeParse
Rules = {
        "S": [["NP", "VP"]],
        "VP": [["VP", "PP"], ["V", "NP"], ["cooks"], ["drinks"], ["eats"], ["cuts"]],
        "PP": [["P", "NP"]],
        "NP": [["Det", "N"], ["he"], ["she"]],
        "V" : [["cooks"], ["drinks"], ["eats"], ["cuts"]],
        "P" : [["in"], ["with"]],
        "N" : [["cat"], ["dog"], ["beer"], ["cake"], ["juice"], ["meat"], ["soup"], ["fork"], ["knife"], ["oven"], ["spoon"]],
        "Det" : [["a"], ["the"]]
        }


def cykParse(w):
    wordAmount = len(w)
     
    
    Table = [[set([]) for wordPos in range(wordAmount)] for i in range(wordAmount)] # Create the table
 
    
    for wordPos in range(0, wordAmount): #For loop, for each word in the original sentence
        print("")
        
        #Checker for terminals
        for lhs, rule in Rules.items(): #lhs is The left part of the rule and rule is the right part of the rule
            for rhs in rule:            #rhs is each list inside a rules
                 
                if len(rhs) == 1 and rhs[0] == w[wordPos]: #Check if the rhs is a word and if the value in rhs equals the word from the sentence
                    Table[wordPos][wordPos].add(lhs) #Add the left part of the rule into T list
 
        for i in range(wordPos, -1, -1):   
            for k in range(i, wordPos + 1):    
                #For loops to check through every spot in the graph

                #Checker for non terminals
                for lhs, rule in Rules.items(): #lhs is The left part of the rule and rule is the right part of the rule
                    for rhs in rule:            #rhs is each list inside a rules
 
                        if len(rhs) == 2:               #Check if its a terminal by seeing length = 2
                            if rhs[0] in Table[i][k]:       #Check if the first terminal in the rhs is in already
                                if(k + 1 < wordAmount): #Checker to make sure there is no index out of range
                                    if rhs[1] in Table[k + 1][wordPos]: #Check if the second terminal is the rhs is in already
                                        Table[i][wordPos].add(lhs)

 
    if len(Table[0][wordAmount-1]) != 0: #Checks if the last cell in the first row is empty or not
        print("True")
        treeParse(w).draw()
    else:
        print("False")
     

# Should be accepted strings
w = "she eats a cake with a fork".split()
# w = "the cat drinks the beer".split()

#Should be rejected strings
# w = "she eats a cake with a spork".split()
# w = "the cat drinks the coke".split()
# w = "hello world".split()

cykParse(w)


