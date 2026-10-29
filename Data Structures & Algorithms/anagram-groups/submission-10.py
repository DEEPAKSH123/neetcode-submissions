class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for word in strs:
            another=[0]*26
            for w in word:
                another[ord(w)-ord('a')]+=1
            res[tuple(another)].append(word)
        return list(res.values())