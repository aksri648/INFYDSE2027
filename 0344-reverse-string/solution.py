def helper(s,start,end):
        if(start>=end):
            return
        s[start],s[end]=s[end],s[start]
        helper(s,start+1,end-1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        helper(s,0,len(s)-1)
        