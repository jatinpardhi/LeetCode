class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.words.reverse()
        self.d = {}
        self.wl = len(words)
        for j in range(len(words)):
            s,e = words[j][0],words[j][-1]
            mv = str([s,e])
            if mv in self.d:
                self.d[mv].append(j)
            else:
                self.d[mv] = [j]
        

    def f(self, prefix: str, suffix: str) -> int:
        s,e = prefix[0],suffix[-1]
        mv = str([s,e])
        res = -1
        if mv in self.d.keys():
            for k in self.d[mv]:
                val = self.words[k]
                if val.startswith(prefix) and val.endswith(suffix):
                    res = k
                    break
        else:
            return -1
        if res == -1:
            return -1
        else:
            return self.wl-res-1
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)