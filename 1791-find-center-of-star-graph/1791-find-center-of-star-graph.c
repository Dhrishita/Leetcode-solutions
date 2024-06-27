int findCenter(int** edges, int edgesSize, int* edgesColSize) {
    int first_edge_0=edges[0][0];
    int first_edge_1=edges[0][1];
    int second_edge_0=edges[1][0];
    int second_edge_1=edges[1][1];
    
    if(first_edge_0==second_edge_0 || first_edge_0==second_edge_1)
    {
        return first_edge_0;
    }
    else
    {
        return first_edge_1;
    } 
}