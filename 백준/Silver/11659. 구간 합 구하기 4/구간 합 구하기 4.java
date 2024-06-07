import java.util.*;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();//횟수
        int n_list[] = new int[n + 1];
        for(int k = 1; k < n_list.length; k++)
            n_list[k] = in.nextInt();
        
        int i[] = new int[m];
        int j[] = new int[m];
        for(int k = 0; k < i.length; k++)
        {
            i[k] = in.nextInt();
            j[k] = in.nextInt();
        }//end for
        //end 입력
        int hap[] = new int[n + 1];
        for (int k = 1; k <= n; k++)
        	hap[k] = hap[k-1] + n_list[k];
        for (int k = 0; k < m; k++)
        	System.out.println(hap[j[k]] - hap[i[k] - 1]);
	}//end main

}//end class
