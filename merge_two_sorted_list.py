def merge( nums1, m, nums2, n) -> None:
    temp=nums1[:m]
    i=0
    j=0
    z=0
    while i<m and j<n:
        if temp[i] <= nums2[j]:
            nums1[z] = temp[i]
            i=i+1
        else:
            nums1[z]= nums2[j]
            j=j+1
        
        z=z+1
    
    while i<m:
        nums1[z]= nums1[i]
        i+=1
        z+=1
    while j<n:
        nums1[z]= nums2[j]
        j+=1
        z+=1
    
    print(nums1)
    return nums1
    
    

    

    

nums1=[1,2,3,0,0,0]
m=3
nums2= [2,5,6]
n=3
merge(nums1,m,nums2,n)