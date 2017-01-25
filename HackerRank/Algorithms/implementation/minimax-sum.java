import java.io.*;
import java.util.*;
public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long sum = 0;
        long[] numbers = new long[5];
        for(int i=0; i<5; i++){
        	numbers[i] = in.nextLong();
        	sum += numbers[i];
        }
        Arrays.sort(numbers);
        String result = ((Long)(sum - numbers[4])).toString() + " " + ((Long)(sum - numbers[0])).toString();
        System.out.println(result);
    }
}
