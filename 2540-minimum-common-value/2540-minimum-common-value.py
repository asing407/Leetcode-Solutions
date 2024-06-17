class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        #common_elements = []
        #for i in range(len(nums1)):
            #for j in range(len(nums2)):
                #if nums1[i] == nums2[j]:
                    #common_elements.append(nums1[i])
        #if common_elements:
            #return common_elements[0]  # Return the first common element as an integer
        #else:
            #return None



        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i +=1 
            else:
                j += 1

        return -1

        