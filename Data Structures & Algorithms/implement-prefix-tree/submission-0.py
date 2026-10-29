class TrieNode():
    def __init__(self):
        self.map={}
        self.islast=False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        cur=self.root
        for w in word:
            if w in cur.map:
                cur=cur.map[w]
            else:
                cur.map[w]=TrieNode()
                cur=cur.map[w]
        cur.islast=True


    def search(self, word: str) -> bool:
        cur=self.root
        for w in word:
            if w not in cur.map:
                return False
            cur=cur.map[w]
        return cur.islast
        

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for w in prefix:
            if w not in cur.map:
                return False
            cur=cur.map[w]
        return True
        
        