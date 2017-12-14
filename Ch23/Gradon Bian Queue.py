## Gradon Bian Queue module
## This is the code of my queue.



##Preset default

NULLPOINTER = -1

class Node:
    def _init_(self):
        self.Data=''
        self.Pointer=NULLPOINTER


##Initialize module begins
def InitialiseQueue():
    Queue=[Node()for i in range (10)]
    HeadElement=NULLPOINTER
    EndElement=NULLPOINTER
    FreeListPointer=0
    for i in range (9):
        Queue[i].Pointer=i+1
    Stack[9].Pointer=NULLPOINTER
    return(Queue,HeadElement,EndElement,FreeListPointer)
    



##Push module begins
def EnterQueue(Queue,HeadElement,FreeListPoitner,NewElement):
    if FreeListPointer != NULLPOINTER:
        NewNodePointer=FreeListPointer
        Queue[NewNodePointer].Data=NewElement
        FreeListPointer=Queue[FreeListPointer].Pointer
        if EndElement==NULLPOINTER:
            HeadElement=NewNodePointer
        else:
            Queue[EndElement].Pointer=NewPointer
        EndElement=NewPointer

    else:
        print("No Space, My Friend.")
    return(Queue,HeadElement,EndElement,FreeListPointer)



##Pop module begins
def LeaveQueue(Queue,HeadElement,EndElement,FreeListPointer):
    if HeadElement!=NULLPOINTER:
        Value = Queue[HeadElement].Data
        ThisNodePointer = Queue[HeadElement].Pointer
    if ThisNodePtr == NULLPOINTER :
        EndElement = NULLPOINTER
        Queue[HeadElement].Pointer = FreeListPointer
        FreeListPointer = HeadElement
        HeadElement = ThisNodePointer
####

        print("Null data.")
        Value=''
    else:
        Value=Stack[TopElement].Data
        ThisNodePointer=TopElement
        TopElement=Stack[TopElement].Pointer
        Stack[ThisNodePointer].Pointer = FreeListPointer
        FreeListPointer=ThisNodePointer
    return (Stack,TopElement,FreeListPointer,Value)

