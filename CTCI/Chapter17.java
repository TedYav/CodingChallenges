import java.util.Scanner;

public class Chapter17{
	public Chapter17(){}

	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int a,b;
		boolean again = true;
		Chapter17 chapter17 = new Chapter17();

		while(again){
			System.out.println("Enter number 1: ");
			a = sc.nextInt();
			System.out.println("Enter number 2: ");
			b = sc.nextInt();
			System.out.println(chapter17.binaryAdd(a,b));
			System.out.println("Again? 1==yes 0==no");
			again = (sc.nextInt() == 1);
		}
	}

	public int binaryAdd(int num1, int num2){
		while(num1 != 0){
			int carry = (num1 & num2) << 1;
			num2 = num1 ^ num2;
			num1 = carry;
		}
		return num2;
	}
}