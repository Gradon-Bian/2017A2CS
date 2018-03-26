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
class vehicle(toy):
    def__init__(self,n,i,p,m,a,b,c,d):
        toy.__init__(self,n,i,p,m)
        self.type=a
        self.height=b
        self.weight=c
        self.length=d
```

### Task 2.5

```python
try:
    if age>0 and age<18:
        self.age=age
    else:
        age=input('please input the age again')
```

### Task 2.6

```python
vehicle=[]
vehicle.append('Red Sports Car','RSC13',15.00,6,'car',3.3,12.1,0.08)
game=[]
game.append('HearthStone','ABC123',328.00,6,'TCG','None')
```

### Task 2.7

```python
def printdetails(id):
   i=0
   while toy[i].id!=id:
        i+=1
   Toy[i].printdetails()
```

### Task 2.8

```python
def discount(n):
    m=n/100
    for i in range(len(toy)):
        toy[i].price=toy[i].price*m

```

### Task 2.9

Even though both the bubble sort and insertion sort algorithms have average case time complexities of O(n2), bubble sort is almost all the time outperformed by the insertion sort. This is due to the number of swaps needed by the two algorithms (bubble sorts needs more swaps). But due to the simplicity of bubble sort, its code size is very small. Also there is a variant of insertion sort called the shell sort, which has a time complexity of O(n3/2), which would allow it to be used practically. Furthermore, insertion sort is very efficient for sorting “nearly sorted” lists, when compared with the bubble sort.

### Task 2.10 

```python
def sort():
       for i in range(len(toys)):
           itemtobeinserted=toy[i]
           n=i-1
           while itemtobeinserted.price<toy[n].price and n>0:
               toy[n+1]=toy[n]
               n-=1
           toy[n+1]=itemtobeinserted


```

