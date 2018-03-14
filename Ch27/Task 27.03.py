## Gradon Bian Opt1
## Task 27.03

class Borrower() :
    def __init__(self, a, b, c) :
        self.__BorrowerName = a
        self.__EmailAddress = b
        self.__BorrowerID = c
        self.__ItemsOnLoan = 0
    def GetBorrowerName(self) :
        return(self.__BorrowerName)
    def GetEmailAddress(self) :
        return (self.__EmailAddress)
    def GetBorrowerID(self) :
        return (self.__BorrowerID)
    def GetItemsOnLoan(self) :
        return(self.__ItemsOnLoan)
    def UpdateItemsOnLoan(self, n) :
        self.__ItemsOnLoan += n
    def PrintDetails(self) :
        print("The borrower is : ", self.__BorrowerName)
        print("Borrower ID : ", self.__BorrowerID)
        print("Email Address: ", self.__EmailAddress)
        print("Items on loan: ", self.__ItemsOnLoan)

NewBorrower = Borrower("Gradon", "123456@qq.com", 654321)
NewBorrower.UpdateItemsOnLoan(6)
NewBorrower.PrintDetails()
NewBorrower.UpdateItemsOnLoan(-3)
NewBorrower.PrintDetails()
