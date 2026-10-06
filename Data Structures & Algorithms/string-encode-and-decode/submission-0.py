class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s)) 
            res+="#"
            res+=s
        return res
    def decode(self, s: str) -> List[str]:
        i=0
        words=[]
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            num=int(s[i:j])
            words.append(s[j+1:j+1+num])
            i=1+j+num
        return words
            