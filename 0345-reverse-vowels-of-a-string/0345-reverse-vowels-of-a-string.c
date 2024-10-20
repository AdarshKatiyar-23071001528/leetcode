bool vowel(char num)
{
    return (num == 'a' || num  == 'e' || num  == 'i' || num == 'o' ||num  == 'u' || num == 'A' || num=='I'||num=='E'||num=='O'||num=='U');
}
char* reverseVowels(char s[])
{ 
    int p = 0;
    int q = strlen(s)-1;
    char temp;
    while(p<q)
    {
        if(vowel(s[p]) && vowel(s[q]))
        {
            temp = s[p];
            s[p]=s[q];
            s[q]=temp;
            p++;
            q--;
        }
        else if (!vowel(s[p]))
        {
            p++;
        }
        else if(!vowel(s[q]))
        {
            q--;
        }
        else
        {
            p++;
            q--;
        }
        
    }
return (s);
}
