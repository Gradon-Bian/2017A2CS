# Gradon Bian S3C5 Opt 1

## Chapter 28 End of Chapter Questions

### Question 1: a 

AND compares the two bits in the same position, if they are both 1, then put 1 in the position of resulted word, other wise put 0.

### Question 1: b

```assembly
AND MASK
MASK: #B00001111
```



### Quesion 1: c 

```assembly
IN 
AND Mask
LSL #4
STO Result 
IN 
AND Mask
OR Result 
STO Result
END 
Mask: #& 0F
```



### Question 2

```assembly
LDR #0
LOOP: IN 
	STX STRING
	ACC IX 
	CMP #33
	JPN LOOP 
ENDLOOP: 
```

