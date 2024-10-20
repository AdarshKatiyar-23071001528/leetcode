void reverseString(char s[], int sSize) {
    int p = 0;
    int q = sSize - 1;
    char tmp;
    //now swap
    for(int i= p; i<q; i++,q--)
    {
        tmp = s[i];
        s[i] = s[q];
        s[q] = tmp;
    }
}