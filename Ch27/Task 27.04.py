## Gradon Bian S3C5 Opt1
## Task 27.04
## Omiting "OnLoan" and "DueDate" attributes that are redundant

class LibraryItem:
    def __init__(self, t, a):
        self.__Title = t
        self.__Author = a
        self.__ItemID = 123
        self.__OnLoan = False

    def GetTitle(self):
        return(self.__Title)
    def GetAuthor(self):
        return(self.__Author)
    def GetItemID(self):
        return(self.__ItemID)
    def GetOnLoan(self):
        return(self.__OnLoan)
    def GetDueDate(self):
        return(self.__DueDate)
    def PrintDetails(self) :
        print("Book title : ", self.__Title)
        print("Author : ", self.__Author)
        print("ID : ", self.__ItemID)
        
class Book(LibraryItem):
    def __init__(self, t, a): 
        LibraryItem.__init__(self, t, a)
    def PrintDetails(self):
        print("Book Details")
        LibraryItem.PrintDetails(self)
        
class Albums(LibraryItem):
    def __init__(self, t, a):
        LibraryItem.__init__(self, t, a)
    def PrintDetails(self):
        print("CD Details")
        LibraryItem.PrintDetails(self)
        

CD1 = Albums('And Justice For All','Metallica')
CD2 = Albums('Dark Side of the Moon','Pink Floyd')
CD3 = Albums('Black Sabbath','Black Sabbath')
CD4 = Albums('All Things Bright and Beautiful','Owl City')
CD5 = Albums('Ocean Eyes','Owl City')

Book1 = Book('12 Rules for Life','Jordan Peterson')
Book2 = Book('White Fang','Jack London')
Book3 = Book('A Song of Ice and Fire','George.R.R.Martin')
Book4 = Book('The Lord of the Rings','J.R.R.Tolkein')



Book4.PrintDetails()
CD5.PrintDetails()




