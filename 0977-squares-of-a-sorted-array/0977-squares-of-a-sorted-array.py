class Solution:
    def sortedSquares(self, s: List[int]) -> List[int]:
        # p = 0
        # q = len(s)-1
        # if(p==q):
        #     s[p]=s[p] * s[p]
        # while(p<q):
        #     s[p]=s[p] * s[p]
        #     s[q]=s[q] * s[q]
        #     p+=1
        #     q-=1
        #     if(p==q):
        #         s[p]=s[p] * s[p]
        # for i in range(0,len(s)):
        #     for j in range(i+1,len(s)):
        #         if(s[i]>s[j]):
        #             temp = s[i]
        #             s[i] = s[j]
        #             s[j] = temp
        s = sorted(x*x for x in s)
        return s