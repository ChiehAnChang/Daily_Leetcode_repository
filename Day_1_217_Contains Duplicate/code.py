class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # since we know that set only requires O(1) look up time, it is good idea to use set.
        seen = set()
    
        for each_num in nums:
            if each_num in seen:
        
                return True
            
            
            seen.add(each_num)


        # Return False iff there is no duplicate at all.
        return False
