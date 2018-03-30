# Gradon Bian S3C5 Opt 1

## Chapter 28 Tasks

### Task 28.01 

```assembly
LDM #2
STO A

LDM #10
STO B

LDD A
ADD B 
STO C 

LDD B 
XOR #&FF
INC ACC 
ADD A 
STO D 
```



### Task 28.02

```assembly
LDD A 
	CMP #0
	JPE ELSE
THEN: 	STO B 
	JMP ENDIF
ELSE:	LDD B 
	DEC ACC 
	STO B 
	JMP ENDIF 
```



### Task 28.03

```assembly
LDM #1
	STO Number
	LDM #0
	STO Total
	LDM #5
	STO Max 
LOOP:	LDD Total 
	ADD Number 
	LDD Number 
	INC ACC 
	STO Number 
	LDD Number 
	CMP Max
	JPN LOOP
ENDLOOP:...
```



### Task 28.04 (Did this wrong) 

```assembly
LDM #0
	STO Count 
LOOP: 	LDD Count
	INC ACC
	STO Count 
	IN 
	CMP #78
	JPN LOOP 
ENDLOOP:...
```



### Task 28.05

```assembly
LDM #0
	STO Count 
LOOP:	LDD Count 
	INC ACC
	STO Count 
	IN 
	CMP #78
	JPN LOOP 
ENDLOOP:LDD Count 
	OUT 
	LDM #0
	STO Count 
LOOP:	LDD Count 
	INC ACC
	STO Count 
	IN 
	CMP #78
	JPN LOOP 
ENDLOOP:LDD Count 
	OUT 
```



### Task 28.06

```assembly
LDD STACKBASE
	STO STACKPTR
LOOP1: IN 
	CMP #13
	STI STACKPTR
	LDD STACKPTR 
	INC ACC 
	STO STACKPTR 
	JMP LOOP1 
LOOP2: LDD STACKPTR 
	CMP STACKBASE 
	JPE ENDWORD 
	LDI STACKPTR 
	OUT 
	LDD STACKPTR 
	DEC ACC 
	STO STACKPTR 
	JMP LOOP2 
ENDWORD: END 
```

