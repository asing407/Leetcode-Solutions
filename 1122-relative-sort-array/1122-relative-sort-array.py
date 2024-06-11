class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        
        for i in arr2:
            for j in range(arr1.count(i)):
                res.append(i)
                if i in arr1:
                    arr1.remove(i)
        return res + sorted(arr1)