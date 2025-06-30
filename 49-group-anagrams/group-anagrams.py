from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap=defaultdict(list)
        for word in strs:
            count=[0]*26
            for ch in word:
                index=ord(ch)-ord('a')
                count[index]+=1
            key=tuple(count)
            hmap[key].append(word)
        return list(hmap.values())