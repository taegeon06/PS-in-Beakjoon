import java.util.*;
import java.io.*;

public class Main {	
	public static void main(String[] args) throws IOException{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(in.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int l = Integer.parseInt(st.nextToken());
		
		Deque<Node> mydeque = new LinkedList<>(); // 덱 생성
		st = new StringTokenizer(in.readLine());
		for (int i = 0; i < n; i++)
		{
			int now = Integer.parseInt(st.nextToken());
			
			while(!mydeque.isEmpty() && mydeque.getLast().value > now) mydeque.removeLast(); // !은 전체 
			
			mydeque.add(new Node(now, i));
			
			if (mydeque.getFirst().index <= i - l) mydeque.removeFirst();
				
			bw.write(mydeque.getFirst().value + " ");
		}// end for
		bw.flush();
		bw.close();
		
	}// end main
static class Node
{
	public int value;
	public int index;
	
	Node(int value, int index)// Node(value, index)
	{
		this.value = value;
		this.index = index;
	}
}
}// end class

