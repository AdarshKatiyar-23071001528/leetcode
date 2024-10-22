def removeSpecial(s):
    chars = "!@#$%^&*()-+?_=,<>/;."
    for char in chars:
        s3 = s.replace(char, "")
    return s3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=''
        s2 = removeSpecial(s)
        s2 =s2.lower()
        for i in s2:
            if len(s2)==2:
                if s2[0]==s2[1]:
                    return True
                else:
                    return False
            elif 48<=ord(i) and 57>=ord(i):
                s1+=i
            elif 97<=ord(i) and 122>=ord(i):
                s1+=i
        r = s1[::-1]
        return(r==s1)