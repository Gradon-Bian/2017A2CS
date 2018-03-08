## Gradon Bian S3C5 Opt1
## [Revised] Task 27.02 （According to the instructions sent through WeChat）
## Only output one from each record. Not using the PrintDetail method, which is redundant.

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

class Book(LibraryItem):
    def __init__(self, t, a): 
        LibraryItem.__init__(self, t, a)
    
class Albums(LibraryItem):
    def __init__(self, t, a):
        LibraryItem.__init__(self, t, a)


CD1 = Albums('And Justice For All','Metallica')
CD2 = Albums('Dark Side of the Moon','Pink Floyd')
CD3 = Albums('Black Sabbath','Black Sabbath')
CD4 = Albums('All Things Bright and Beautiful','Owl City')
CD5 = Albums('Ocean Eyes','Owl City')

Book1 = Book('12 Rules for Life','Jordan Peterson')
Book2 = Book('White Fang','Jack London')
Book3 = Book('A Song of Ice and Fire','George.R.R.Martin')
Book4 = Book('The Lord of the Rings','J.R.R.Tolkein')



FavBookN=Book4.GetTitle()
FavBookA=Book4.GetAuthor()
FavMusN=CD5.GetTitle()
FavMusS=CD5.GetAuthor()

print("Among the listed 4 books, my favorite one is:",FavBookN,"Written by",FavBookA)
print("Of the 5 CDs, I particularly enjoy:",FavMusN,",singer is",FavMusS)


