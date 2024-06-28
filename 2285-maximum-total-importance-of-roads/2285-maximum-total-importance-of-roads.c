typedef struct 
{
    int city;
    int degree;
} CityDegree;
int compare(const void *a, const void *b) 
{
    return ((CityDegree*)b)->degree - ((CityDegree*)a)->degree;
}
long long maximumImportance(int n, int** roads, int roadsSize, int* roadsColSize) {
    CityDegree *cityDegrees=(CityDegree*)malloc(n*sizeof(CityDegree));
    for (int i=0;i<n;i++) 
    {
        cityDegrees[i].city=i;
        cityDegrees[i].degree=0;
    }
    for (int i=0;i<roadsSize;i++) 
    {
        cityDegrees[roads[i][0]].degree++;
        cityDegrees[roads[i][1]].degree++;
    }
    qsort(cityDegrees,n,sizeof(CityDegree),compare);
    int *values=(int*)malloc(n*sizeof(int));
    for (int i=0;i<n;i++) 
    {
        values[cityDegrees[i].city]=n-i;
    }
    long long totalImportance = 0;
    for (int i=0;i<roadsSize;i++) 
    {
        totalImportance+=values[roads[i][0]]+values[roads[i][1]];
    }
    free(cityDegrees);
    free(values);  
    return totalImportance;
}