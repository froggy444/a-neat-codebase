def mergeSortedArrays(nums1, nums2,m,n):
   last = m + n -1 #llast index of nums1
   
   while m > 0 and n > 0: #merge in the reverse order
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1
    
    #fill nums1 with leftover elements of nums2
            
   while n > 0:
       nums1[last] = nums2[n - 1]
       n, last = n - 1, last - 1

   print(nums1)
    
    



