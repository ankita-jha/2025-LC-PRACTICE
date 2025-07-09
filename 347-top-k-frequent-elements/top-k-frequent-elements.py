class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        for i in nums:
            if i not in hmap:
                hmap[i]=1
            else:
                hmap[i]+=1
        heap=[]
        for key, val in hmap.items():
            heapq.heappush(heap,(val,key))
            if len(heap)>k:
                heapq.heappop(heap)
        return [key for val,key in heap]
