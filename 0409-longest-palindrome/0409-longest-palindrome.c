int longestPalindrome(char* s) {
    int charCount[128] = {0}; 
    int length = 0;
    int oddCount = 0;

    for (int i = 0; s[i] != '\0'; i++)
    {
        charCount[s[i]]++;
    }
    for (int i = 0; i < 128; i++) 
    {
        if (charCount[i] % 2 == 0) 
        {
            length += charCount[i];
        } 
        else 
        {
            length += charCount[i] - 1;
            oddCount = 1; 
        }
    }
    return length + oddCount;
}
    
