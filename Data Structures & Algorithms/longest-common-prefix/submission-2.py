class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        minlength=float("+inf")
        for s in strs:
            minlength=min(minlength,len(s))

        i=0
        while i<minlength:
            first = strs[0][i]
            stop = False
            for j in range(len(strs)):
                if strs[j][i] != first:
                    stop=True
                    break
                
            if stop:
                return res 
            res = res + first

                


            i+=1
        return res