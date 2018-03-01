# Gradon Bian S3C5 Opt 1

## Chapter 26 End of Chapter Questions

### Question 1: a i

```python
class CustomerRecord :

	def __init__(self) :

		self.CustomerID = 0

		self.CustomerName = ''

		self.TelNumber = ''

		self.TotalOrders = 0

```

### Question 1: a ii

```python
CustomerData = [CustomerRecord() for i in range(1000)]
```



### Quesion 1: b i

```python
def Hash(ID) :
	Address = ID % 1000
	return (Address)
```



### Question 1: b ii (I did this wrong)

```python
def AddRecord(CustomerData, Customer):
	Address = Hash(Customer.CustomerID)
	while CustomerData(Address).CustomerID != 0 :
		Address = Address + 1
		if Address = 1000 :
			Address = 0
	CustomerData[Address] = Customer
```



### Question 1: b iii

```python
def FindRecord(CustomerData, ID):
	Address = Hash(ID)
	while CustomerData[Address].CustomerID != ID :
		Address = Address + 1
        if Address = 1000 :
			Address = 0
	return (Address)
```



### Question 1: c

```python
import pickle
def SaveData(CustomerData) :
	CustomerFile = open('CustomerData.Dat','wb')
	for i in range(1000) :
		pickle.dump(CustomerData[i], CustomerFile)
	CustomerFile.close()
```



### Question 1: d (I did this wrong)

Need to set up fixed length dummy records and save them to a random file.
AddRecord needs to update the correct record in the random file.
FindRecord needs to read the random file. Don’t need the SaveData procedure at the end of program execution



### Question 2

```python
def OpenFile() :
	FileName = input("Which file do you want to use? ")
	try:
		FileHandle = open(FileName, 'rb+')
	except :
		print("File does not exist")
```



