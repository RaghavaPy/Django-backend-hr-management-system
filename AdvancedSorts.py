def merge_sort(arr):
    if len(arr)<=1:   #base condition
        return arr  
    middle=len(arr)//2     #middle Element
    left=arr[:middle]
    right=arr[middle:]
    left=merge_sort(left)  #recursivelry sort left part 
    right=merge_sort(right) #recursivelry sort right part
    return merge(left,right)
def merge(left,right):
    result=[]
    i=0
    j=0 
    while i<len(left) and j<len(right):
        if left[i] <=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result
arr=[38,27,43,3,9,82,24,56,19,10]  
sorted_Arr=merge_sort(arr)       
print(f"Sorted Array is : {sorted_Arr}")           

# qucik sort lumto partiton
def quick_sort(arr,low,high):
    if low<high:
        pivotIndex=partiton(arr,low,high)
        quick_sort(arr,low,pivotIndex-1)
        quick_sort(arr,pivotIndex+1,high) 

def partiton(arr,low,high):
    pivot=arr[high]        
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
             i+=1
             arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
arr=[1,5,8,9,2,4,6,16]
quick_sort(arr,0,len(arr)-1)  
print(arr)      

def hoare_partion(arr,low,high):
    if low<high:
        partition=horare(arr,low,high)
        hoare_partion(arr,low,partition)
        hoare_partion(arr,partition+1,high)
def horare(arr,low,high):
    pivot=arr[low]
    left=low-1
    right=high+1
    while True:
        while True:
            left+=1
            if arr[left]>=pivot:
                break           
        while True:
            right-=1
            if arr[right]<=pivot:
                break            
        if left>=right:
            return right
        arr[left],arr[right]=arr[right],arr[left] 
arr=[6,3,8,1,2,10,5,9,41,15,11]      
hoare_partion(arr,0,len(arr)-1)    
print(arr)     

#counting sort
def Counting_sort(arr):
    if len(arr)<=1:
        return arr
    max_value=max(arr)
    min_value=min(arr)
    range_value = max_value - min_value + 1
    count=[0]*range_value
    print(f"count is {count}")
    for num in arr:
        count[num-min_value]+=1
    print(f"After counting array is {count}")
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    print(f"After the cummulative array is {count}")
    output=[0]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        num=arr[i]
        index=num-min_value
        output[count[index]-1]=num
        count[index]-=1
    return output
arr=[2,5,7,9,3,56,89,91,1,66,5,5,2]
sorted_array=Counting_sort(arr)
print(f"{sorted_array}")     

def radix_counting(exp,arr):
    n=len(arr)
    print(f"{n},length")
    print(f"{arr}")
    output=[0]*n
    count=[0]*10
    for i in range(n):
       digit=(arr[i]//exp)%10
       count[digit]+=1
    print(f"countDigi:t{count}")
    for i in range(1,10):
        count[i]+=count[i-1]   
    print(f"cummulative:{count}")    
    for i in range(n-1,-1,-1):
        digit=(arr[i]//exp)%10   
        output[count[digit]-1]=arr[i]
        count[digit]-=1
    print(f"output array : {output}")    
    for i in range(n):
        arr[i]=output[i]
def radix_sort(arr):
    if len(arr)<=1:
        return arr
    max_value=max(arr)        
    print(f"{max_value}")           
    exp=1
    print(max_value//exp,"<-value")
    while max_value//exp>0:
        radix_counting(exp,arr)
        exp*=10
    return arr
arr = [170, 45, 75, 90, 802, 24, 2, 66]

print("Before sorting:")
print(arr)

radix_sort(arr)

print("After sorting:")
print(arr)    

#Bucket sort for the floating values between the range of 0 to 1
def bucket_sort(arr):
    if len(arr)==0:
        return arr
    n=len(arr)
    buckets=[[] for i in range(n)]
    print(f"buckets{buckets}")
    for num in arr:
        index=int(n*num)
        print(f"index:{index}")
        if index==n:
            index=-1
        buckets[index].append(num)
    for bucket in buckets:
        print(f"before sort bucket : {bucket}")
        bucket.sort()
        print(f"After sort bucket : {bucket}")
    result=[]
    for bucket in buckets:
        result.extend(bucket)
    return result    
arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51] 
print(bucket_sort(arr))     

#bucket sort for the arbitary numbers
def bucket_integers(arr):
    if len(arr)==0:
        return arr
    n=len(arr)
    max_value=max(arr)
    min_value=min(arr)
    buckets=[[] for i in range(n)]
    bucket_size=(max_value-min_value)/n+1
    for num in arr:
        index=int((num-min_value)/bucket_size)
        buckets[index].append(num)
    results=[]
    for bucket in buckets:
        results.extend(bucket)
    return results
arr = [42, 5, 18, 30, 11]
sorted_arr=bucket_integers(arr)
print(f"Final bucket sort array is : {sorted_arr}")    
           
    
   
            
        