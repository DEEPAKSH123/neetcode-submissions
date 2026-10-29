class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add=1
        r=len(digits)-1
        while add:
            if r>=0:
                if digits[r]!=9:
                    digits[r]+=add
                    add=0
                else:
                    digits[r]=0
                    r-=1
                    add=1
            else:
                digits.insert(0,1)
                add=0
        return digits

        