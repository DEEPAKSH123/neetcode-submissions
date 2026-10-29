class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for w in strs:
            encoded+= str(len(w)) + "#" + w
        
        return encoded

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0

        while i < len(s):
            j=i
            while s[j]!= "#":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+length+1])
            i=j+length+1
        return res
