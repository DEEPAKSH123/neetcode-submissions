class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1={}
        map2={}
        true=True
        false=False
        if(len(s)!=len(t)):
            return false
        for letter in s:
            map1[letter]=map1.get(letter,0)+1
        for letter in t:
            map2[letter]=map2.get(letter,0)+1
        for key in map1:
            if map1[key]!=map2.get(key,0):
                return false
        return true


            
            

    

        