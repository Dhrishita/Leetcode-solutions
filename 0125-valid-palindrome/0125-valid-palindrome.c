bool isAlphanumeric(char c)
{
    return isalnum(c);
}
bool isPalindrome(char* s) {
    int left=0;
    int right = strlen(s)-1;
    
    while(left<right)
    {
        while(left<right && !isAlphanumeric(s[left]))
        {
            left++;
        }
         while(left<right && !isAlphanumeric(s[right]))
        {
            right--;
        }
        if(tolower(s[left])!= tolower(s[right]))
        {
            return false;
        }
        left++;
        right--;
    }
    return true;
}