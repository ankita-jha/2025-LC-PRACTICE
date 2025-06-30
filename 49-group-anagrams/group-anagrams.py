class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap={}
        for i in strs:
            word=''.join(sorted(i))
            if word not in hmap:
                hmap[word]=[i]
            else:
                hmap[word].append(i)
        print(hmap)
        # return all the values
        output=[]
        for key in hmap.keys():
            output.append(hmap[key])
        print(output)
        return output