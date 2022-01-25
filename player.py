from math import log2

AMT = 5 #default word size in Wordle
WORDS = "wordlist.txt" #word list in the directory as source, via reddit
OPTS = "allowed.txt" #permitted guesses beyond target words
rankDict ={} #rank value for each allowable word. later extend to midgame.
wordDict={} #just the target words, T/F if still in contention

def colors(guess, target):
    result = ["x"]*5 # using array since strings immutable
    for i in range(AMT):
        if guess[i]==target[i]:
            result[i]="G"
        elif guess.count(guess[i]) <= target.count(guess[i]):
            result[i]="Y" #pretty sure this matches actual Wordle rules...
    return "".join(result)

def makelist(solsFile, allowFile):
    global rankDict, wordDict
    for readFile in [solsFile, allowFile]:
        wordfile = open(readFile, "r")
        ans = wordfile.read().split()
        wordfile.close()
        for a in ans:
            rankDict[a]=float("inf") #lower number is best choice for next word
            if readFile == solsFile:
                wordDict[a]=True # True = possible word, False = impossible at midgame
    return

def entropy(guess, curr):
    matches={}
    for pot in curr:
        code = colors(guess,pot)
        if code not in matches.keys():
            matches[code]=1
        else:
            matches[code]+=1
    ent = 0
    for code in matches.keys():
        ent += matches[code]*log2(matches[code])
    return ent

def cull(currWord, code):
    for x in wordDict.keys(): # no need for [w for w in wordDict.keys() if wordDict[w]] since don't want to scan over twice
        if wordDict[x]:
            if colors(currWord,x) != code:  #nested if rather than "and" to insure short-circuiting
                wordDict[x]=False

def main():
    makelist(WORDS, OPTS)
    code = ""
    count=0 #num of guesses used so far
    newWord = "soare" #discovered by preprocessing
    while code != "GGGGG":
        count +=1
        msg = "enter colors for guess #" + str(count)+ " "+newWord + ": "
        code = input(msg)
        cull(newWord,code)
        current = [ x for x in wordDict.keys() if wordDict[x] ] # only checks the still viable target words
        minim = float("inf") #current smallest ent
        newWord = "" #current next guess
        for w in rankDict.keys(): #testing strength as a first word
            rankDict[w]=entropy(w, current)
            if rankDict[w] < minim or (rankDict[w] == minim and w in current and newWord not in current):
                newWord = w
                minim = rankDict[w]
    print("we won Wordle in",count,"guesses!")

if __name__ == '__main__':
    main()
