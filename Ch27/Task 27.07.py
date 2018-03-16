## Gradon Bian S3C5 Opt1
## Task 27.07
## Revised using the mark scheme of the book. Highlighted my mistakes.
## No output and instances of data.


import datetime

class Borrower:
    def __init__(self, a, b, c): # constructor
        self.__BorrowerName = a
        self.__EmailAddress = n
        self.__BorrowerID = c
        self.__ItemsOnLoan = 0
    def GetBorrowerName(self):
        return(self.__BorrowerName)
    def GetEmailAddress(self):
        return(self.__EmailAddress)
    def GetBorrowerID(self):
        return(self.__BorrowerID)
    def GetItemsOnLoan(self):
        return(self.__ItemsOnLoan)
    def UpdateItemsOnLoan(self, n):
        self.__ItemsOnLoan = self.__ItemsOnLoan + n
    def PrintDetails(self):
        print(self.__BorrowerName, ';', self.__BorrowerID, ';', end='')
        print(self.__EmailAddress, ';', self.__ItemsOnLoan)


class LibraryItem:
    def __init__(self, t, a, i):
        self.__Title = t
        self.__Author = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__BorrowerID = 0
        self.__DueDate = datetime.date.today()##I did this wrong.

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
    def GetIsRequested(self):
        return(self.__IsRequested)
    def Returning(self,m,n):
        self.OnLoan = False
        n.UpdateItemsOnLoan(-1)
    def PrintDetails(self) :
        print(self.__Title, ';', self.__Author_Artist, ';', end =' ')
        print(self.__ItemID, ';', self.__OnLoan, ';', end = ' ')
        print(self.__BorrowerID, ';', self.__DueDate)

class Book(LibraryItem):
    def __init__(self, t, a, i): # I did wrong for this part
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = 0
    def GetIsRequested(self):
        return(self.__IsRequested)
    def GetRequestedBy(self):
        return(self.__RequestedBy)
    def RequestBook(self, i, x):
        self.__IsRequested = True
        self.__RequestedBy = x.GetBorrowerID()
    def PrintDetails(self):
        LibraryItem.PrintDetails(self)
        print(self.__IsRequested, ';', self.__RequestedBy)

class CD(LibraryItem):
    def __init__(self, t, a, i): # Containment
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""
    def GetGenre(self):
        return(self.__Genre)
    def SetGenre(self, g):
        self.__Genre = g
    def PrintDetails(self):
        LibraryItem.PrintDetails(self)
        print(self.__Genre)


        

CD1 = Albums('And Justice For All','Metallica')
CD2 = Albums('Dark Side of the Moon','Pink Floyd')
CD3 = Albums('Black Sabbath','Black Sabbath')
CD4 = Albums('All Things Bright and Beautiful','Owl City')
CD5 = Albums('Ocean Eyes','Owl City')

Book1 = Book('12 Rules for Life','Jordan Peterson')
Book2 = Book('White Fang','Jack London')
Book3 = Book('A Song of Ice and Fire','George.R.R.Martin')
Book4 = Book('The Lord of the Rings','J.R.R.Tolkein')










