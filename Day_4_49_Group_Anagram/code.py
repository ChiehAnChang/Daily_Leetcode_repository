class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in d:
                d[sorted_s].append(s)
            else:
                d[sorted_s] = [s]
        return list(d.values())