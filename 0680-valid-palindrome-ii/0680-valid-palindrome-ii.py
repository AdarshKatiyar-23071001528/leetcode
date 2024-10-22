def reverse(s):
    s3 = s[::-1]
    return s3
def replace(n,x):
    x1 = ''
    for i in range (0,len(x)):
        if i!=n:
            x1+=x[i]
    return x1
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            p = 0
            q = len(s)-1
            count=0
            while(p<q):
                if(s[p]==s[q]):
                    count=1
                    p+=1
                    q-=1
                else:
                # count-=2
                # p+=1
                # q-=1
                    
                    s1 = replace(p,s)
                    s2 = replace(q,s)
                    if s1 == reverse(s1):
                        return True
                    else:
                        # s2 = s.replace(s[q],"",1)
                        if s2 == reverse(s2):
                            return True
                        else:
                            return False
            
        
#         s1=''
#         s2 = removeSpecial(s)
#         s2 = s2.lower()
#         count = 0
#         if len(s2) %2 == 0:
#             count = 0
#         else:
#             count+=1
#         p = 0
#         q = len(s2)-1
#         while(p<q):
#             if(s2[p]==s2[q]):
#                 # count+=2
#                 p+=1
#                 q-=1
#             else:
#                 count-=2
#                 p+=1
#                 q-=1
#         if count>=0:
#             return True
#         else:
#             count = 0
#             if len(s2) %2 == 0:
#                 count = 0
#             else:
#                 count+=1
#             p = 1
#             q = len(s2)-1
#             while(p<q):
#                 if(s2[p]==s2[q]):
#                     count+=2
#                     p+=1    
#                     q-=1
#                 else:
#                     count-=2
#                     p+=1
#                     q-=1
#             if count>=0:
#                 return True
#             else:
#                 count = 0
#                 if len(s2) %2 == 0:
#                     count = 0
#                 else:
#                     count+=1
#                 p = 0
#                 q = len(s2)-2
#                 while(p<q):
#                     if(s2[p]==s2[q]):
#                         count+=2
#                         p+=1
#                         q-=1
#                     else:
#                         count-=2
#                         p+=1
#                         q-=1
#                 if count>=0:
#                     return True
#                 else:
#                     # m = 1
#                     # n = len(s2)-2
#                     # while(m<n):
#                     #     s4 = s2.replace(s2[m], "")
#                     return False

#         # for i in s2:
#         #     if (len(s2)==4):
#         #         if(s2[0]==s2[3]):
#         #             return True
#         #         else:
#         #             return False
#         #     # if 65<=ord(i) and 90>=ord(i):
#         #     #     n = ord(i)+32
#         #     #     s1+=chr(n)
#         #     elif len(s2)==2:
#         #         if s2[0]==s2[1]:
#         #             return True
#         #         else:
#         #             return False
#         #     elif 48<=ord(i) and 57>=ord(i):
#         #         s1+=i
#         #     elif 97<=ord(i) and 122>=ord(i):
#         #         s1+=i
#         # r = s1[::-1]
#         # return(r==s1)