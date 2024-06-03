int appendCharacters(char* s, char* t) {
    int i=0,j=0;
    int slen= strlen(s);
    int tlen=strlen(t);

    while(i<slen && j<tlen)
    {
        if(s[i]==t[j])
        {
            j++;
        }
        i++;
    }
    if(j==tlen)
    {
        return 0;
    }
    return tlen-j;
}