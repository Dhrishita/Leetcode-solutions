class Solution {
  public double averageWaitingTime(int[][] customers) {
    double wait = 0;
    double current = 0;

    for (int[] d : customers) 
    {
      current = Math.max(current, 1.0 * d[0]) + d[1];
      wait+= current-d[0];
    }
    return 1.0 * wait/customers.length;
  }
}