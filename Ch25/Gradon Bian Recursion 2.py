## Gradon Bian S3C5 Opt1
## Recursion 2
## No input or output, just functions with returns

def groupSum(start,nums,target):
    if target==0:
        return True
    if start==len(num):
        return False
    return groupSum(start+1,nums,taget) or groupSum(start+1,nums,target)

def groupSum6(start,nums,target):
    if start>=len(nums):
        return target==0
    if nums[start]==6:
        return groupSum6(start+1,nums,target-nums[start])
    return groupSum6(start+1,nums,target-nums[start]) or groupSum6(start+1,nums,target)

def groupNoAdj(start,nums,target):
    if start>=len(num):
        return target==0
    return groupNoAdj(start+2,nums,target-nums[start]) or groupNoAdj(start+1,nums,target)

def groupSum5(start,nums,target):
    if start>=len(nums):
        return target==0
    if nums[start]%5==0:
        if start<len(num)-1 and nums[start+1]==1:
            return groupSum5(start+2,nums,target-nums[start])
        return groupSum5(start+1,nums,target-nums[start])
    return groupSum5(start+1,nums,target-nums[start]) or groupSum5(start+1,nums,target)

def groupSumClump(start,nums,target):
    if start>=len(nums):
        return target==0
    sum=nums[start]
    count=1
    i=start+1
    for i in range (len(nums)):
        if nums[i]==nums[start]:
            sum=sum+nums[i]
            count=count+1
        i=i+1
    return groupSumClump(start+count,nums,target-sum) or groupSumClump(start+count,nums,target)

## splitArray function begins

def helper(start,nums,sum1,sum2):
    if start>=len(nums):
        return sum1==sum2
    return helper(start+1,nums,sum1+nums[start],sum2) or helper(start+1,nums,sum1,sum2+nums[start])
      
def splitArray(nums):
    return helper(0,nums,0,0)

## splitArray funcion ends

## splitOdd10 function begins

def helper1(start,nums,sum1,sum2):
    if start>=len(nums):
        return (sum1%10==0 and sum2%2==1) or (sum1%2==1 and sum2%10==0)
    return helper1(start+1,nums,sum1+nums[start],sum2) or helper2(start+1,nums,sum1,sum2+nums[start])

def splitOdd10(nums):
    return helper1(0,nums,0,0)
## splitOdd10 function ends

## split53 function begins

def helper2(start,nums,sum1,sum2):
    if start>=len(nums):
        return sum1==sum2
    if nums[start]%5==0:
        return helper2(start+1,nums,sum1+nums[start],sum2)
    if nums[start]%3==0:
        return helper2(start+1,nums,sum1,sum2+nums[start])
    return helper2(start+1,nums,sum1+nums[start],sum2) or helper2(start+1,nums,sum1,sum2+nums[start])

def split53(nums):
    return helper2(0,nums,0,0)

## split53 function ends



        
