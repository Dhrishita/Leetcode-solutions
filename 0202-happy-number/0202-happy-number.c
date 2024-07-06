int sumofsquares(int n)
{
    int sum=0;
    while(n>0)
    {
        int digit=n%10;
        sum+=digit*digit;
        n/=10;
    }
    return sum;
}
bool isHappy(int n) {
    int current_digit=n, square_of_current_digit=n;
    do
    {
        current_digit=sumofsquares(current_digit);
        square_of_current_digit=sumofsquares(sumofsquares(square_of_current_digit));
    }
    while(current_digit!=square_of_current_digit);
    return current_digit==1;
}