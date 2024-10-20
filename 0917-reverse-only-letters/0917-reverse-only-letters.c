
char* reverseOnlyLetters(char s[]) {
    int p = 0;
    int q = strlen(s)-1;
    char temp;
    int count,count1;
    while(p<q)
    {
        count = 0;
        count1 = 0;
        if( (s[p]>='a' && s[p]<='z') || (s[p]>='A' && s[p]<='Z'))
        {
            count+=1;
        }
        if( (s[q]>='a' && s[q]<='z') || (s[q]>='A' && s[q]<='Z'))
        {
            count1+=1;
        }


        if((count==1) && (count1==1))
        {
        temp = s[p];
        s[p] = s[q];
        s[q] = temp;
        p++;
        q--;
        }
        else if(count!=1)
        {
        p++;
        }
        else if (count1!=1)
        {
        q--;
        }
        else
        {
        p++;
        q--;
        }
    }
    return s;
}