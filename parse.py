import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
S -> NP VP
VP -> VP PP
VP -> V NP
VP -> 'cooks' | 'drinks' | 'eats' | 'cuts'
PP -> P NP
NP -> Det N
NP -> 'he' | 'she'
V -> 'cooks' | 'drinks' | 'eats' | 'cuts'
P -> 'in' | 'with'
N -> 'cat' | 'dog'
N -> 'beer' | 'cake' | 'juice' | 'meat' | 'soup'
N -> 'fork' | 'knife' | 'oven' | 'spoon'
Det -> 'a' | 'the'
""")

def treeParse(w):
    a = []
    parser = nltk.ChartParser(grammar)
    for tree in parser.parse(w):
        a.append(tree)
    return(a[0])