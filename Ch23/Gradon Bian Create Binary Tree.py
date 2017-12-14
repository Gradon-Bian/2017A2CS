# Gradon Bian S3C5 Opt1 CS
# This is my python code to create a new binary tree (with insert and find modules)
# There is no input or output module in this code
# Coded with the aid of the pseudocode on the textbook

NULLPOINTER=-1
class TreeNode:
    def _init_(self):
        self.Data= ""
        self.LeftPointer=NULLPOINTER
        self.RightPointer=NULLPOINTER

def InitializeTree():
    Tree=[TreeNode for i in range (9)]
    RootPointer=NULLPOINTER
    FreePointer=0
    for i in range (8):
        Tree[i].LeftPointer=i+1
    Tree[9].RightPointer=NULLPOINTER

def InsertNode(NewItem):
    if FreePointer != NULLPOINTER:
        NewNodePointer=FreePointer
        FreePointer=Tree[FreePointer].LeftPointer
        Tree[NewNodePointer].LeftPointer=NULLPOINTER
        Tree[NewNodePointer].RightPointer=NULLPOINTER
    if RootPointer==NULLPOINTER:
        RootPointer=NewNodePointer
        ThisNodePointer=RootPointer
        while ThisNodePointer != NULLPOINTER:
            PreviousNodePointer = ThisNodePointer
            if Tree[ThisNodePointer].Data > NewItem:
                TurnedLeft=True
                ThisNodePointer=Tree[ThisNodePointer].LeftPointer
            else:
                TurnedLeft=False
                ThisNodePointer=Tree[ThisNodePointer].RightPointer
        if TurnedLeft==Ture:
            Tree[PreviousNodePointer].LeftPointer=NewNodePointer
        else:
            Tree[PreviousNodePointer].RightPointer=NewNodePointer


def FindNode(SearchItem):
    ThisNodePointer=RootPoitner
    while ThisNodePointer!=NULLPOINTER and Tree[ThisNodePointer].Data != SearchItem:
        if Tree[ThisNodePointer].Data>SearchItem:
            ThisNodePointer=Tree[ThisNodePointer].LeftPointer
        else:
            ThisNodePointer=Tree[ThisNodePointer].RightPointer
    return ThisNodePointer




            
    
    
