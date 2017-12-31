## Gradon Bian S3C5 Opt 1
## Christmas Holiday Project: Word Count Tool (Using Dictionary)
## This program can identify the words that appear more than twice in a given text, and list them out with the number of times they appear
## This program can also list the words in both Dictionary order, and Alphabetical order (for the ease of reading).

## 2017/12/31



def getNum(x):
    return x[1]

def main():
    txt=input("Please input a text in ENGLISH: ")
    wordCount={}
    for e in txt:
        if e in "! ; . \t\n\"()-:#@$":
            txt=txt.replace(e,',')
    L=txt.split(',')
    L.sort()
    while L[0].isdigit() or L[0]=='':
        del L[0]
    for e in L:
        if e in wordCount:
            wordCount[e]=wordCount[e]+1
        else:
            wordCount[e]=1
            
    print("[Dictionary order]Words that appear for more than 2 times and the times they appear: ")
    words=list(wordCount.keys())
    words.sort()
    for e in words:
        if wordCount[e]>2:
            print(e,wordCount[e])

    print("[Alphabetical order]Words that appear for more than 2 times and the times they appear:")
    L1=list(wordCount.items())
    L1.sort(key=getNum,reverse=True)
    for i in range (len(L1)):
        if L1[i][1]>2:
            print(L1[i][0],L1[i][1])

main()



