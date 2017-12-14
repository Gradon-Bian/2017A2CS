## Gradon Bian S3C5 Opt 1 CS
## Hash Table
## Programmed with the aid of the pseudocode on the textbook

## NOT YET FINISHED! (Still missing a initiation of the class of the hash table)


## Insert a record into a hash table

def Insert(NewRecord):
    Index=Hash(NewRecord.Key)
    while Hashtable[Index] not empty:
        Index=Index+1
        if Index>Max:
            Index=1
    HashTable[Index]=NewRecord


## Find a record in a hash table

def FindRecord(SearchKey):
    while HashTable[Index].Key!=SearchKey and HashTable[Index] not empty:
        Index = Index +1
        if Index>Max:
            Index=0
    if HashTable[Index] not empty:
        return HashTable[Index]


## To be continued.....
