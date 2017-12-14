## Gradon Bian Stack module
## This is the code of my stack, which can insert an element at the beginning of the stack and pop.



##Preset default

NULLPOINTER = -1

class Node:
    def _init_(self):
        self.Data=''
        self.Pointer=NULLPOINTER


##Initialize module begins
def InitialiseStack():
    Stack=[Node()for i in range (10)]
    TopElement=NULLPOINTER
    FreeListPointer=0
    for i in range (9):
        Stack[i].Pointer=i+1
    Stack[9].Pointer=NULLPOINTER
    return(Stack,TopElement,FreeListPointer)
    



##Push module begins
def PushStack (Stack,TopElement,FreeListPoitner,NewElement):
    if FreeListPointer != NULLPOINTER:
        NewNodePointer=FreeListPointer
        Stack[NewNodePointer].Pointer=TopElement
        FreeListPointer=Stack[FreeListPointer].Pointer
        Stack[NewNodePointer].Pointer=TopElement
        TopElement=NewNodePointer
    else:
        print("No Space, My Friend.")
    return(Stack,TopElement,FreeListPointer)



##Pop module begins
def Pop(Stack,TopElement,FreeListPointer):
    if TopOfStack==NULLPOINTER:
        print("Null data.")
        Value=''
    else:
        Value=Stack[TopElement].Data
        ThisNodePointer=TopElement
        TopElement=Stack[TopElement].Pointer
        Stack[ThisNodePointer].Pointer = FreeListPointer
        FreeListPointer=ThisNodePointer
    return (Stack,TopElement,FreeListPointer,Value)

