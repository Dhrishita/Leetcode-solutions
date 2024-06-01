int reverse(int x){
    int rev_no=0;
    while(x!=0)
    {
        int last_digit = x%10;
        x=x/10;
        if(rev_no> INT_MAX/10 || (rev_no==INT_MAX/10 && last_digit >7)) return 0;

        if(rev_no< INT_MIN/10 || (rev_no==INT_MIN/10 && last_digit <-8)) return 0;
        rev_no = (rev_no * 10)+last_digit;
    }
    return rev_no;
}