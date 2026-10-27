class Solution:
    def isAnagram(self, s1: str, s2: str) -> bool:
        res = {}
        if len(s1)!=len(s2):
            return False
        for k in range(len(s1)):
            if s1[k] not in res:
                res[s1[k]] = 1
            else:
                res[s1[k]]+=1
            if s2[k] not in res:
                res[s2[k]] = -1
            else:
                res[s2[k]]-=1
        for key, value in res.items():
            if value != 0:
                return False
        return True
#
'''
s = "racecar", t = "carrace"
dics ={r:1}, dict[{c:1}
dics ={r:1,a:1}, dict{c:1, a:1}
dics ={r:1,a:1,c:1}, dict{c:1, a:1, r:1}
dics ={r:1,a:1,c:1,e:1}, dict{c:1, a:1, r:2,}
dics ={r:1,a:1,c:2,e:1}, dict{c:1, a:2, r:2,}
dics ={r:1,a:2,c:2,e:1}, dict{c:2, a:2, r:2,}
dics ={r:2,a:2,c:2,e:1}, dict{c:2, a:2, r:2,e:1}

loop2- s = "racecar"
    j=r
    dics[r] != dict[t]

dic for s and dic for t
loop for lenght of s for both s and t
if that character is in the dic, then increment
loop for elements of s:
if dics[key] != dict[key]

'''