## Gradon Bian S3C5 Opt 1
## This is the CodingBat code for Recursion 1 (to "changePi")
## All should be working correctly
## There is no input or output, only the functions

# 2017/12/07


def factorial(n):
    if n==1:
        return 1
    else:
        return(n*factorial(n-1))

def bunnyEars(n):
    if n==0:
        return 0
    else:
        return (2+bunnyEars(n-1))
 

def fibonacci(n):
    if n==0:
        return 0
    else:
        return (n+fibonacci(n-1))


def bunnyEars2(n):
    if n==0:
        return 0
    else:
        return (2.5+bunnyEars2(n-1))


def triangle(n):
    if n==0:
        return 0
    else:
        return (n+triangle(n-1))



def sumDigits(n):
    if n==0:
        return 0
    else:
        return ((n%10)+int(sumDigits(n/10)))


def Count7(n):
    if n==0:
        return 0
    if n%10 == 7:
        return (1+Count7(n/10))
    return Count7(n/10)
        
        
def Count8(n):
    if n==0:
        return 0
    if (n>=88) and n%100 == 88:
        return (2+Count8(n/10))
    if n%10==8:
        return (1+Count8(n/10))
    return Count8(n/10)

def powerN(base,n):
    if n==0:
        return 0
    return (base*powerN(base,n-1))

def countX(str):
    result = 0
    if len(str)==0:
        return 0
    if str[0]=='x':
        result=result+1
    result = countX(str[1:len(str)])+result
    return result


def countHi(str):
    result=0
    if len(str)<=2:
        if str=='hi':
            return 1
        return 0

    if str[0:2]=='hi':
        result=result+1
        str=str[2:len(str)]
    else:
        str=str[1:len(str)]
    result=result+countHi(str)
    return result

def changeXY(str):
    result=''
    if len(str)==0:
        return ''
    if str[0]=='x':
        result='y'
    else:
        result = str[0]
    return result+changeXY(str[1:len(str)])

def changePi(str):
   result=''
   if len(str)<2:
       return str
   if str[0]=='p' and str[1]=='i':
       result='3.14'
       str=str[2:len(str)]
   else:
       result=str[0]
       str=str[1:len(str)]
   return result+changePi(str)

def noX(str):
    result=''
    if len(str)==0:
        return ''
    if str[0]=='x':
        result = ''
    else:
        result=str[0]
    return result+noX(str[1:len(str)])

def array6(nums,index):
    if index>=len(nums):
        return False
    elif nums[index]==6:
        return True
    else:
        return (array6(nums,index+1))

def array11(nums,index):
    result=0
    if index>=len(nums):
        return 0
    if nums[index]==11:
        result=result+1
    result=result+array11(nums,index+1)
    return result

def array220(nums,index):
    if index>=len(nums):
        return False
    elif nums[index]*10==nums[index+1]:
        return True
    else:
        return array220(nums,index+1)

def allStar(str):
    result=''
    if len(str)==1 or len(str)==0:
        return str
    else:
        result=result+(str[0]+'*')
    result=result+allStar(str[1:len(str)])
    return result

def pairStar(str):
    result=''
    if len(str)<=1:
        return str
    if str[0]==str[1]:
        result=result+str[0]+'*'
    else:
        result=result+str[0]
    result=result+pair(Star)(str[1:len(str)])
    return result

## endX Module
def endX(str):
    result=''
    x= countX(str)
    result=noX(str)
    result=result+addX(x)
    
def addX(num):
    if num<1:
        return ''
    if num==1:
        return 'x'
    return 'x'+addX(num-1)
## End



def countPairs(str):
    result=0
    if len(str)<=2:
        return 0
    if str[0]==str[2]:
        result=result+1
    result=result+countPiars(str[2:len(str)])
    return result

def countAbc(str):
    result=0
    if len(str)<=2:
        return 0
    if str[0:3]=='aba' or str[0:3]=='abc':
        result=result+1
    result=result+countAbc(str[1:len])
    return result

def count11(str):
    result=0
    if len(str)<=1:
        return 0
    if str[0:2]=='11' or str[0:2]=='11':
        result=result+1
        str=str[2:len(str)]
    else:
        str=str[1:len(str)]
    result=result+count11(str)
    return result

def stringClean(str):
    if len(str)<=1:
        return str
    result=''
    c=str[0]
    n=''

    while n==c and len(str)>1:
        if n==c:
            str=str[1:len(str)]
        if len(str)<=1:
            break
    n=str[1]
    if len(str)>=1:
        str=str[1:len(str)]
    result=result+c
    result=result+stringClean(str)
    return result

def countHi2(str):
    result=0
    if len(str)<2:
        return 0
    elif len(str)==2:
        if str=='hi':
            return 1
        else:
            return 0
    else:
        if str[0]=='x':
            if len(str)<=3:
                return 0
            elif str[1:3]=='hi':
                str=str[3:len(str)]
            else:
                str=str[1:len(str)]
        else:
            if str[0:2]=='hi':
                result=result+1
                str=str[2:len(str)]
            else:
                str=str[2:len(str)]
    result=result+countHi2(str)
    return result

def parenBit(str):
    result=''
    if str[0]=='(':
        if str[len(str)-1]==')':
            return str
        else:
            return parenBit(str[0:len(str)-1])
    else:
        return parenBit(str[1:len(str)])

def nestParen(str):
    result=''
    if len(str)==0:
        return True
    if len(str)<1:
        return False
    if str[0]=='(':
        if str[len(str)-1]==')':
            return nestParen(str[1:len(str)-1])
        return False
    else:
        return False

def strCount(str,sub):
    result=0
    if len(str)<len(sub):
        return 0
    elif len(str)==len(sub) and str==sub:
        return 1
    elif str[0:len(str)]==sub:
        result=result+1
        str=str[len(sub):len(str)]
    else:
        str=str[1:len(str)]
    result=result+strCount(str,sub)
    return result

def strCopies(str,sub,n):
    if strCount(str,sub)==n:
        return True
    else:
        return False
    str=str[1:len(str)]
    result=result+strCount(str,sub)
    return result

def strDist(str,sub):
    if len(str)==1 and str==sub:
        return 1
    elif len(str)<len(sub) or len(str)<=1:
        return 0
    else:
        if str[0]==sub[0] and str[0]==str[len(str)-len(sub)] and str[len(str)-len(sub):len(str)]==sub and str[len(str)-len(sub)]==sub:
            return len(str)
        else:
            if str[0:len(sub)]==sub:
                return strDist(str[1:len(str)-1],sub)
            elif str[len(str)-len(sub):len(str)]==sub:
                return strDist(str[1,len(str)],sub)
            return strDist(str[1:len(str)-1],sub)    


            
