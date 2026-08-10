class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l=0 
        need={}
        dic = {}
        for i in range(len(s1)):
            need[s1[i]]=need.get(s1[i],0)+1
        for i in range(len(s2)):
            dic[s2[i]]=dic.get(s2[i],0)+1
            while i - l +1>len(s1):
                dic[s2[l]]-=1
                if dic[s2[l]] == 0:
                    del dic[s2[l]]
                l+=1

            if need == dic:
                return True
        
        return False
