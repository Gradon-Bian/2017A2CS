## Gradon Bian S3C5 Opt1
## Task 23.05
## Omitted DueDate
class Borrower() :
    def __init__(self, t, a, i): 
        self.__Title = t
        self.__Author_Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__BorrowerID = 0
    def GetBorrowerName(self) :
        return (self.__BorrowerName)

    def GetEmailAddress(self) :
        return (self.__EmailAddress)

    def GetBorrowerID(self) :
        return (self.__BorrowerID)

    def GetItemsOnLoan(self) :
        return (self.__ItemsOnLoan)

    def Borrowing(self, b):
        self.__OnLoan = True
        self.__BorrowerID = b
    def PrintDetails(self):
        print(self.__Title, ' ; ',self.__Author_Artist, ' ; ', end='')
        print(self.__ItemID, ' ; ', self.__OnLoan)
        



NewBorrower = Borrower("Gradon", "abc@qq.com", 123)
NewBorrower.PrintDetails()

