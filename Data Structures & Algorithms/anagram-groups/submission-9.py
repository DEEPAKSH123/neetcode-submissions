class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res=[]
        dict=collections.defaultdict(list)
        for string in strs:
            arr=[0]*26
            for i in range(len(string)):
                arr[ord(string[i])-ord('a')]=arr[ord(string[i])-ord('a')]+1
            dict[tuple(arr)].append(string)
            
        return list(dict.values())