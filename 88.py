def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = len(nums1)-1
    j = m-1
    k = n-1
    while k>=0:
        if j<0 or nums2[k]>nums1[j]:
            nums1[i] = nums2[k]
            k -= 1
        else:
            nums1[i] = nums1[j]
            j -= 1
        i -= 1
    print(nums1)
        
if __name__ == '__main__':
    print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
    print(merge([1],1,[],0))
    print(merge([0],0,[1],1))
