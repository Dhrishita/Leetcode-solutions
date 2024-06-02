bool isSubsequence(char* s, char* t) {
    int i,j;
    int slen = strlen(s);
    int tlen = strlen(t);
    for(i=0, j=0; j<tlen;j++)
    {
        if(i<slen && s[i]==t[j])
        {
            i++;
        }
    }
    return i==slen;
}


