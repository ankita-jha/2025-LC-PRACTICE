class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hmap={}
        # for i in nums:
        #     if i not in hmap:
        #         hmap[i]=1
        #     else:
        #         hmap[i]+=1
        # heap=[]
        # for key, val in hmap.items():
        #     heapq.heappush(heap,(val,key))
        #     if len(heap)>k:
        #         heapq.heappop(heap)
        # return [key for val,key in heap]
        '''
        bucket sort
        '''
        hmap={}
        for i in nums:
            if i not in hmap:
                hmap[i]=1
            else:
                hmap[i]+=1
        print(hmap)
        freq=[[] for i in range(len(nums)+1)]
        for key, val in hmap.items():
            freq[val].append(key)
        print(freq)
        res=[]
        for i in range(len(freq)-1,0,-1):
            print(freq[i])
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res