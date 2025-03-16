class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        freq = Counter(nums)  # Step 1
        
        # Step 2: 建立桶
        max_freq = len(nums)  # 元素最多出現次數不會超過 n
        bucket = [[] for _ in range(max_freq + 1)]
        
        # Step 3: 放入對應桶
        for num, count in freq.items():
            bucket[count].append(num)
        
        # Step 4: 從後往前收集答案
        result = []
        for count in range(max_freq, -1, -1):  # 從 n, n-1, ..., 1, 0
            if bucket[count]:
                for num in bucket[count]:
                    result.append(num)
                    if len(result) == k:
                        return result
