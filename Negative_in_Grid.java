import java.util.*;
public class NegativeNumbers
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int m=sc.nextInt();
        int[][] grid=new int[n][m];
        for( int i=0 ;i < n ;i++)
        {
            for (int j= 0 ; j < n ; j ++)
            {
                 grid[i][j]=sc.nextInt();
            }
        }
        int cnt=0;
        for (int i= 0; i < n ; i ++)
        {
            for( int j=0; j< n; j++)
            {
                if (grid[i][j]<0)
                    cnt+=1;
            }
        }
        System.out.println(cnt);
    }
}
