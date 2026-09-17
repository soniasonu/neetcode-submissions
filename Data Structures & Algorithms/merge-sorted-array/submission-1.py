class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        arr = []
        for i in range(m):
            arr.append(nums1[i])
        for j in range(n):
            arr.append(nums2[j])
        arr.sort()
        for i in range(m+n):
            nums1[i] = arr[i]
    
