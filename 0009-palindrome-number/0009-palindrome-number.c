bool isPalindrome(int x) {
    long rev_no=0;
    int dhrishita = x;
    while(x>0)
    {
        int last_digit = x%10;
        rev_no = (rev_no*10)+last_digit;
        x=x/10;
    }
    return dhrishita ==rev_no;
}