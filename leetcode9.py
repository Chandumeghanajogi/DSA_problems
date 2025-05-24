def mountain(arr):
    n=len(arr)
    if n<3:
        return False
    else:
        peak=0
        for i in range(0,n-1):
            if arr[i]<arr[i+1]:
                peak=i+1
        
        if peak==0 or peak==n-1:
            return False
        
        for i in range(peak):
            if arr[i]>=arr[i+1]:
                return False
        for j in range(peak,n-1):
            if arr[j]<=arr[j+1]:
                return False
        return True
    
arr = [1,3,2]
print(mountain(arr))

