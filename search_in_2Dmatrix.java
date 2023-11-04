import java.util.*;
public class SearchMatrix
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int m=sc.nextInt();
        int[][] arr=new int[n][m];
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                arr[i][j]=sc.nextInt();
            }
        }
        int c = 0;
        int s=sc.nextInt();
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(arr[i][j]==s)
                {
                    System.out.println("true");
                    c = 1;
                    break;
                } 
            }
        }
        if(c==0) 
        {
            System.out.println("false");
        }
    }
}
