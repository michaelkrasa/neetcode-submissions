class Solution:

    def encode(self, strs: List[str]) -> str:
        # include number of characters and a special characted in the resultatnt string
        return "".join(f"{len(s)}|{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        # 5|hello
        # how do we recognize the length of the number?
        # need to find the delimiter first and then create an int from the numbers inbetween i and j
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "|":
                j += 1
            s_len = int(s[i:j])
            res.append(s[j + 1: j + 1 + s_len])
            i = j + 1 + s_len

        return res



            

        

