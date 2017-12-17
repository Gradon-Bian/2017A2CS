# End of Chapter Questions : Ch 25
## Gradon Bian S3C5 Opt 1
###1. a
Iteration is executing the same set of instructions a given number of times or until a specified result is obtained. Recursion is the process of repeating a function, each time applying it to the result of the previous stage

###1. b
Advantage: the code is really concise and easy to write for solving certain questions that requires recursion.
Disadvantage: if the recursion is too deep (or too long), the stack frames (or space occupied) may become too full.

###2. a
In the definition, there is a call of itself.

### 2. b
|Call Number  | Procedure Call      | Exponent=0 | Result
| ------------- |:-------------:| :-----:|---------:|
| 1      | Power(2,4) | False |
| 2     | Power(2,3)     |  False | 
| 3 |Power(2,2) |False | 
|4 |Power(2,1) |False|
|5|Power(2,0)|True|1
|(4)|Power(2,1)||2
|(3)|Power(2,2)||4
|(2)|Power(2,3)||8
|(1)|Power(2,4)||16

### 2. c
When the procedure is called, the return address and the values of the local variables and the partial result of the calculation are stored on the stack. When the base case of Exponent=0 reached, the result is stored on the stack.This unwinding continues until the place in the program that called Power(2,4) is returned to.

### 2. e
```pseudocode
FUNCTION Power(Base : INTEGER, Exponent : INTEGER) RETURNS INTEGER
	Result ¡û 1
	WHILE Exponent > 0
		Result ¡û Result * Base
		Exponent ¡û Exponent - 1
	ENDWHILE
	RETURN Result
ENDFUNCTION
```
### 2. f i
Non-recursive function is easier to understand for the users, as it does not contain many logical operations.

### 2. f ii
It reflects the mathematical solution to a problem, which is logical and concise.

### 3. a i
Line 04 is the base case

### 3. a ii
Line 06 is the base case

### 3. b
|Call Number  | Procedure Call      | n | (n=0)OR(n=1)|Result
| :------------- |:-------------:| :-----:|:---------:|------:|
| 1 | Fibonacci(4) |4| FALSE |
| 2  | Fibonacci(3)|3 |  FALSE| 
| 3 |Fibonacci(2)|2 |FALSE| 
|4 |Fibonacci(1) |1|TRUE|1
|5|Fibonacci(0)|0|TRUE|0
|(3)||2||1
|6|Fibonacci(1)|1|TRUE|1
|(2)||3||2
|7|Fibonacci(2)|2|FALSE|
|8|Fibonacci(1)|1|TRUE|1
|9|Fibonacci(0)|0|TRUE|0
|(7)||2||1
|(1)||4||3


> Written with [StackEdit](https://stackedit.io/).