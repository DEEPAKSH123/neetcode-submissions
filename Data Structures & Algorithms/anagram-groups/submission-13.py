class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict=defaultdict(list)
        for word in strs:
            alpha=[0]*26
            for letter in word:
                alpha[ord(letter)- ord('a')]+=1
            dict[tuple(alpha)].append(word)
        return list(dict.values())
        