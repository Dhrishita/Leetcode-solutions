int passThePillow(int n, int time) {
    int current_holder=1;
    int direction=1;
    for(int i=0;i<time;i++)
    {
        current_holder+=direction;
        if(current_holder==n)
        {
            direction=-1;
        }
        else if(current_holder==1)
        {
            direction=1;
        }
    }
    return current_holder;
}