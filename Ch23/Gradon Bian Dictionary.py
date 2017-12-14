##Gradon Bian Opt 1 S3C5
## Not Yet Finished!!

class NewRecord:
    def __init__(x):
        x.Key=''
        x.Value=''

List=[(NewRecord())for i in range (26)]


def Hash(key):
    a=ord(Key[0])-65
    return a


def AddEntry(Word,Def):
    a=Hash(x.Word)
    while WordDef[a].Key != '':
        a=a+1
        if a>26:
            a=0
    WordDef[a]=Entry

def Return(Word):
    Index=Hash(Word)
    while (WordDef[a].Key != Word) and (WordDef[a] != ''):
        a=a+1
        if a>26:
            Index=0
    if WordDef[a]!='':
        return WordDef[a].Value
    else:
        return "Does not exist"






















## Ignore this part/




##Insert record into a hash table
def Insert(NewRecord):
    Index=Hash(NewRecord.Key)
    if Index>26:
        Index=1
    HashTable[Index]=NewRecord

def FindRecord(SearchKey):
    Index=Hash(SearchKey)
    while (List[Index].Key!=SearchKey) and (List[Index] != ''):
        Index=Index+1
        if Index>26:
            Index=0

    if HashTable[Index] not emtpy:
        return HashTable[Index]































































    


def Return(Found):
    Index=Hash(Found)
    while(
        )
