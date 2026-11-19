class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        target=sorted(s1)

        for r in range(len(s2)):
            while r-l+1>len(s1):
                l+=1
            if sorted(s2[l:r+1]) == target:
                return True
        return False