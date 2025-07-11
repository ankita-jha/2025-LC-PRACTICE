class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap=defaultdict(list)
        for word in strs:
            count=[0]*26
            for char in word:
                index=ord(char)-ord('a')
                count[index]+=1
            key=tuple(count)
            hmap[key].append(word)
        return list(hmap.values())