##Gradon Bian S3C5 Opt1 CS
##This is my completed FreeList python program (without input and output)
##Done with reference to the pseudocode on the book.

class ListNode:
    def __init__(self) :
        self.Data = ""
        self.Pointer = NULLPOINTER
    
def InitialiseList() :
    List = [ListNode() for i in range(9)]
    StartPointer = NULLPOINTER 
    FreeListPointer = 0 
    for Index in range(8):
        List[Index].Pointer = Index + 1
    List[8].Pointer = NULLPOINTER 
    return(List, StartPointer, FreeListPointer)

def InsertNode(List, StartPointer, FreeListPointer, NewItem) :
    if FreeListPointer != NULLPOINTER :
        NewNodePointer = FreeListPointer
        List[NewNodePointer].Data = NewItem
        FreeListPointer = List[FreeListPointer].Pointer
        PreviousNodePointer = NULLPOINTER
        ThisNodePointer = StartPointer 
        while ThisNodePointer != NULLPOINTER and List[ThisNodePointer].Data < NewItem :
            PreviousNodePointer = ThisNodePointer 
            ThisNodePointer = List[ThisNodePointer].Pointer

        if PreviousNodePointer == NULLPOINTER :
            List[NewNodePointer].Pointer = StartPointer
            StartPointer = NewNodePointer
        else : 
            List[NewNodePointer].Pointer = List[PreviousNodePointer].Pointer
            List[PreviousNodePointer].Pointer = NewNodePointer
    else :
        print("no space, my friend.")
    return(List, StartPointer, FreeListPointer)


def FindNode(List, StartPointer, DataItem):
    CurrentNodePointer = StartPointer 
    while CurrentNodePointer != NULLPOINTER and List[CurrentNodePointer].Data != DataItem :
        CurrentNodePointer = List[CurrentNodePointer].Pointer
    return(CurrentNodePointer)


def DeleteNode(List, StartPointer, FreeListPointer, DataItem) :
    ThisNodePointer = StartPointer 
    while ThisNodePointer != NULLPOINTER and List[ThisNodePointer].Data != DataItem:
        PreviousNodePointer = ThisNodePointer
        ThisNodePointer = List[ThisNodePointer].Pointer
    if ThisNodePointer != NULLPOINTER : 
        if ThisNodePointer == StartPointer : 
            StartPointer = List[StartPointer].Pointer
        else :
            List[PreviousNodePointer].Pointer = List[ThisNodePointer].Pointer
        List[ThisNodePointer].Pointer = FreeListPointer
        FreeListPointer = ThisNodePointer
    else :
        print("data does not exist!!")
    return(List, StartPointer, FreeListPointer)
