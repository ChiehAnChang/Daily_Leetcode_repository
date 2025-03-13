class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # since this question looks for the check the number of the letter occurance, we should use the dictionary.
        
        d = dict()
        for each_letter in s:
            if each_letter in d:
                d[each_letter] += 1
            else:
                d[each_letter] = 1
        
        for each_letter in t:
            if( each_letter not in d) or (d[each_letter] == 0) or (len(s)!=len(t)):
                return False
            else:
                d[each_letter] -= 1
        return True
