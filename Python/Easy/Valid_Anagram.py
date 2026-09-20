class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S=dict()
        T=dict()
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            S[s[i]]=S.get(s[i], 0) + 1
            T[t[i]]=T.get(t[i], 0) + 1
        if S==T:
            return True
        return False
