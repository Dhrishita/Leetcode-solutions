int compare(const void *a,const void *b)
{
    return (*(int*)a - *(int*)b);
}
int minMovesToSeat(int* seats, int seatsSize, int* students, int studentsSize) {
    qsort(seats,seatsSize,sizeof(int),compare);
    qsort(students,studentsSize,sizeof(int),compare);
    int Min_moves =0;
    for(int i=0;i<seatsSize;i++)
    {
        Min_moves+=abs(students[i]-seats[i]);
    }
    return Min_moves;
}