int numWaterBottles(int numBottles, int numExchange) {
    int total_drunk=numBottles, empty_bottles=numBottles;
    while(empty_bottles>=numExchange)
    {
       int full_bottle=empty_bottles/numExchange;
        total_drunk+=full_bottle;
        empty_bottles=(empty_bottles%numExchange)+full_bottle;
    }
    return total_drunk;
}