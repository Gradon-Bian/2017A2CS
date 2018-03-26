# CS Prerelease Material#

##S3C5 Gradon Bian Opt1

###Task 1.1###

JSP structures programs and data in terms of sequences, iterations and selections, and as a consequence it is applied when designing a program's detailed control structure.

### Task 1.2###

"*": means repetition, the repeating procedure will not continue to the next step of the structure unless the repetition is completed.

"°"：means selection, so there will be multiple senarios connected at the base of this procedure leading to an extension of the structure.

### Task 1.3###

NOT EndOfFile (Not sure about thi)

Salary>50

Salary>=90

ProjectManager

LeadDeveloper

Manager

### Task 1.4###

*[See Attached picture for the graph!]*

### Task 1.5###

```pseudocode
WHILE NOT EndOfFile:
	CALL ReadSalary()
	IF Salary>50
		THEN
			IF Salary>70
				THEN
					IF Salary>=90
						THEN
							Role←ProjectManager
						ELSE
							Role←Consultant
					ENDIF
				ELSE
					Role←LeadDeveloper
			ENDIF
		ELSE
			Role←Manager
	ENDIF
```



### Task 1.6

```python
def DetermineRole(Salary):
    if Salary>50:
        if Salary>70:
            if Salary>=90:
                Role="Project Manager"
            else:
                Role="Consultant"
        else:
            Role="Lead Developer"
   	else:
        Role="Manager"
	return(Role)
        
        
```



### Task 2.1

*[See Attached picture for the graph!]*

### Task 2.2

Inheritance: all attributes and  me tho ds  of  the  base class are copied to the subclass

(Arrows completed in Task 2.1)

### Task 2.3

```python
class Toy:
    def __init__(self):
        self.__Name=''
        self.__ID=0
        self.__Price=0.00
        self.__MinimumAge=0
    def SetName(self,n):
        self.__Name=n
    def SetID(self,i):
        self.__ID=i
    def SetPrice(self,p):
        self.__Price=p
    def SetMinimumAge(self,m):
        self.__MinimumAge=m
    def GetName(self):
        return(self.__Name)
    def GetID(self):
        return(self.__ID)
    def GetPrice(self):
        return(self.__Price)
    def GetMinimumAge(self):
        return(self.__MinimumAge)
    
```

### Task 2.4

```python
class ComputerGame(Toy):
    def __init__(self):
        Toy.__init__(self)
        self.__Category=''
        self.__Console=''
    def SetCategory(self,c):
        self.__Category=c
    def SetConsole(self,m):
        self.__Console=m
    def GetCategory(self):
       	return(self.__Category)
  	def GetConsole(self):
        return(self.__Console)

class Vehicle(Toy):
    def __init__(self):
        Toy.__init__(self)
        self.__Type=''
        self.__Height=0
        self.__Length=0
        self.__Weight=0.0
    def SetType(self,c):
        self.__Type=c
    def SetHeight(self,m):
        self.__Height=m
    def SetLength(self,n):
        self.__Length=n
    def SetWeight(self,i):
        self.__Weight=i
    def GetType(self):
       	return(self.__Type)
  	def GetHeight(self):
        return(self.__Height)  
    def GetLength(self):
       	return(self.__Length)
  	def GetWeight(self):
        return(self.__Weight) 
```

### Task 2.5

```python
class Toy:
    def __init__(self):
        self.__Name=''
        self.__ID=0
        self.__Price=0.00
        self.__MinimumAge=0
    def SetName(self,n):
        self.__Name=n
    def SetID(self,i):
        self.__ID=i
    def SetPrice(self,p):
        if p<=100:
        	self.__Price=p
    def SetMinimumAge(self,m):
        if m<=18:
            self.__MinimumAge=m
    def GetName(self):
        return(self.__Name)
    def GetID(self):
        return(self.__ID)
    def GetPrice(self):
        return(self.__Price)
    def GetMinimumAge(self):
        return(self.__MinimumAge)
class ComputerGame(Toy):
    def __init__(self):
        Toy.__init__(self)
        self.__Category=''
        self.__Console=''
    def SetCategory(self,c):
        self.__Category=c
    def SetConsole(self,m):
        self.__Console=m
    def GetCategory(self):
       	return(self.__Category)
  	def GetConsole(self):
        return(self.__Console)

class Vehicle(Toy):
    def __init__(self):
        Toy.__init__(self)
        self.__Type=''
        self.__Height=0
        self.__Length=0
        self.__Weight=0.0
    def SetType(self,c):
        self.__Type=c
    def SetHeight(self,m):
        if m<=30:
        	self.__Height=m
    def SetLength(self,n):
        if n<=50:
        	self.__Length=n
    def SetWeight(self,i):
        if i<=100:
        	self.__Weight=i
    def GetType(self):
       	return(self.__Type)
  	def GetHeight(self):
        return(self.__Height)  
    def GetLength(self):
       	return(self.__Length)
  	def GetWeight(self):
        return(self.__Weight) 
```

### Task 2.6

```python
Array=[]
Car1=Vehicle()
Car1.SetName('Red Sports Car')
Car1.SetID('RSC13')
Car1.SetPrice('15.00')
Car1.SetMinimumAge('6')
Car1.SetType('Car')
Car1.SetHeight(3.3)
Car1.SetLength(12.1)
Car1.SetWeight(0.08)
Array.append(Car1)
Game1=ComputerGame()
Game1.SetName('HearthStone')
Game1.SetID('ABC123')
Game1.SetPrice('328.00')
Game1.SetMinimumAge('6')
Game1.SetCategory('TCG')
Game1.SetConsole('None')
Array.append(Game1)
```

### Task 2.7

```python
ID=input("Please input ID for the toy:")
for i in range 5:
    if ID==Array[i].ID:
        print(Array[i].GetName())
        print(Array[i].GetID())
        print(Array[i].GetPrice())
        print(Array[i].GetMinimumAge())
        print(Array[i].GetCatgory())
        print(Array[i].Get.GetConsole())     
```

### Task 2.8

```python
Discount=int(input("Please input discount rate: "))
class Toy:
    def __init__(self):
        self.__Name=''
        self.__ID=0
        self.__Price=0.00
        self.__MinimumAge=0
    def SetName(self,n):
        self.__Name=n
    def SetID(self,i):
        self.__ID=i
    def SetPrice(self,p):
        if p<=100:
        	self.__(Price=p*Discount)/100
    def SetMinimumAge(self,m):
        if m<=18:
            self.__MinimumAge=m
    def GetName(self):
        return(self.__Name)
    def GetID(self):
        return(self.__ID)
    def GetPrice(self):
        return(self.__Price)
    def GetMinimumAge(self):
        return(self.__MinimumAge)
class ComputerGame(Toy):
    def __init__(self):
        Toy.__init__(self)
        self.__Category=''
        self.__Console=''
    def SetCategory(self,c):
        self.__Category=c
    def SetConsole(self,m):
        self.__Console=m
    def GetCategory(self):
       	return(self.__Category)
  	def GetConsole(self):
        return(self.__Console)

class Vehicle(Toy):
    def __init__(self):
        Toy.__init__(self)
        self.__Type=''
        self.__Height=0
        self.__Length=0
        self.__Weight=0.0
    def SetType(self,c):
        self.__Type=c
    def SetHeight(self,m):
        if m<=30:
        	self.__Height=m
    def SetLength(self,n):
        if n<=50:
        	self.__Length=n
    def SetWeight(self,i):
        if i<=100:
        	self.__Weight=i
    def GetType(self):
       	return(self.__Type)
  	def GetHeight(self):
        return(self.__Height)  
    def GetLength(self):
       	return(self.__Length)
  	def GetWeight(self):
        return(self.__Weight) 

```

### Task 2.9

Even though both the bubble sort and insertion sort algorithms have average case time complexities of O(n2), bubble sort is almost all the time outperformed by the insertion sort. This is due to the number of swaps needed by the two algorithms (bubble sorts needs more swaps). But due to the simplicity of bubble sort, its code size is very small. Also there is a variant of insertion sort called the shell sort, which has a time complexity of O(n3/2), which would allow it to be used practically. Furthermore, insertion sort is very efficient for sorting “nearly sorted” lists, when compared with the bubble sort.

### Task 3.0 

（didn't really understand the question, so put on the bubble sort solution）
```python
MyList = []
for Index in range(7):
	MyList.append( int(input("Enter a number: ")))
MaxIndex = 7
n = MaxIndex - 1
NoMoreSwaps = False
	while NoMoreSwaps == False:
		NoMoreSwaps = True
		for j in range(n):
			if MyList[j] > MyList[j + 1]:
				Temp = MyList[j]
				MyList[j] = MyList[j + 1]
				MyList[j + 1] = Temp
				NoMoreSwaps = False
		n = n - 1
for Index in range(7):
	print(MyList[Index])





```