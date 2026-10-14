class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Setu = {}
        aai = []

        for saks in nums:
            Setu[saks] = 1 + Setu.get(saks, 0)
        # Sort based on Values
        sorted_dict = {k: v for k, v in sorted(Setu.items(), key=lambda item: item[1], reverse=True)}
# item[1] represents the sorting based on value
        
        for i, key in enumerate(sorted_dict):
            if i == k:  # Stop after k elements
                break
            aai.append(key)

        return aai


