##BinarySearch Python (Gradon Bian Opt1)##

def binarySearch(arr,value):
    found=False
    searchFail=False
    low=0
    high=len(arr)-1
    while not found and not searchFail:
        middle=int((low+high)/2)
        if arr[middle]==value:
            found=True
        else:
            if low>=high:
                searchFail=True
            else:
                if arr[middle]>value:
                    high=middle-1
                else:
                    low=middle+1
    if found:
        return middle
    else:
        return -1
