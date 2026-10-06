class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp={} # val : index
        mp2={}
        for i,n in enumerate(s):
            if n in mp:
                mp[n]+=1
            else:
                mp[n]=1
        for j,k in enumerate(t):
            if k in mp2:
                mp2[k]+=1
            else:
                mp2[k]=1
        if len(mp)==len(mp2):
            for key in mp:
                if key not in mp2 or mp[key]!=mp2[key]:
                    return False
            return True
        return False