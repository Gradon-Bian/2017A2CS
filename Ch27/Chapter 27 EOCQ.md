# Gradon Bian S3C5 Opt 1

## Chapter 27 End of Chapter Questions

### Question 1: a 

###[Difficult to draw using markdown, so please see attached photo]###

### Question 1: b

```python
class BankAccount :
	def __init__(self, m): 
		self.__AccountHolderName = ''
		self.__IBAN = i
	def SetAccountHolderName(self, n):
		self.__AccountHolderName = n
	def GetAccountHolderName(self):
		return(self.__AccountHolderName)
	def GetIBAN(self):
		return(self.__IBAN)
```



### Quesion 1: c i (bold one is for what I did wrong)

Attributes: MonthlyFee, OverDraftLimit

Methods: **Constructor**, GetMontlyFee, GetOverDraftLimit, SetOverDraftLimit



### Question 1: c ii (bold one is for what I did wrong)

Attributes: InterestRate

Methods: **Constructor**, CalculateInterest



### Question 1: c iii

Encapsulations



### Question 2: a

[SeasonTicketHolder]:

EmailAddress: STRING

GetEmailAddress()

GetTicketHolderName()



[Pay-As-You-Go-TicketHolder]: (bold is for what I did wrong)

PRIVATE

Amount: **CURRENCY**

PUBLIC

Constructor(Name: STRING, Email: STRING)

GetAmount()
UpdateAmount()

[ContractTicketHolder]: (bold is for what I did wrong)

PRIVATE
MonthlyFee : **CURRENCY**

PUBLIC
Constructor(Name: STRING, Email : STRING, Fee : CURRENCY)
GetFee()



### Question 2: b i

They can only be changed in class methods, and will not be altered when called in other places.



### Question 2: b ii

They can be used to access class attributes anywhere through code easily.



### Question2: c##

```python
NewCustomer = ContractTicketHolder("A. Smith","xyz@abc.xx", 10)
```


### Question3: a##
Containment

### Question3: b##
```python
class NodeClass :
	def __init__(self):
		self.__Data = ''
		self.__Pointer = -1
	def SetData(self, m):
		self.__Data = m
	def GetData(self):
		return(self.__Data)
	def SetPointer(self, x):
		self.__Data = x
	def GetPointer(self):
		return(self.__Pointer)
```


### Question3: c

```python
class QueueClass :
	def __init__(self):
		self.__Queue = [NodeClass() for i in range(51)]
		self.__Head = -1
		self.__Tail = -1
```



### Question3: d (I did this one wrong)

```python
def JoinQueue(self, x):
	if Head == -1 :
		Head = 0
	self.__Tail += 1 
	i = self.__Tail
	self.__Queue[i].SetData(x)
```

