class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        ans = []

        for num in freq:
            if freq[num] >= k:
                ans.append(num)

        return ans