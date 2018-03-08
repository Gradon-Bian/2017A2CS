## Gradon Bian S3C5 Opt1
## Task 27.02
## Only output one from each record.

class Books:
    def __init__(self,m,n):
        self.__BookName=m
        self.__BookAuthor=n
    def GetBookName(self):
        return(self.__BookName)
    def GetBookAuthor(self):
        return(self.__BookAuthor)

class Albums:
    def __init__(self,a,b):
        self.__AlbumName=a
        self.__Singer=b
    def GetAlbumName(self):
        return(self.__AlbumName)
    def GetSinger(self):
        return(self.__Singer)

CD1 = Albums('And Justice For All','Metallica')
CD2 = Albums('Dark Side of the Moon','Pink Floyd')
CD3 = Albums('Black Sabbath','Black Sabbath')
CD4 = Albums('All Things Bright and Beautiful','Owl City')
CD5 = Albums('Ocean Eyes','Owl City')

Book1 = Books('12 Rules for Life','Jordan Peterson')
Book2 = Books('White Fang','Jack London')
Book3 = Books('A Song of Ice and Fire','George.R.R.Martin')
Book4 = Books('The Lord of the Rings','J.R.R.Tolkein')

FavBookN=Book4.GetBookName()
FavBookA=Book4.GetBookAuthor()
FavMusN=CD5.GetAlbumName()
FavMusS=CD5.GetSinger()

print("Among the listed 4 books, my favorite one is:",FavBookN,"Written by",FavBookA)
print("Of the 5 CDs, I particularly enjoy:",FavMusN,",singer is",FavMusS)
