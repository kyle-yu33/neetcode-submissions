class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1, freq2= {}, {}
        l=0 

        for n in s1:
            freq1[n]=1+freq1.get(n,0)

        for r in range(len(s2)):
            while r-l+1>len(s1):
                freq2[s2[l]]-=1

                if freq2[s2[l]]==0:
                    del freq2[s2[l]]
                l+=1
            freq2[s2[r]]=1+freq2.get(s2[r],0)

            if freq1==freq2:
                return True
        return False
            
