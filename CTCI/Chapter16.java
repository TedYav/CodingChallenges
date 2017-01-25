import java.util.Scanner;

public class Chapter16 {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int a,b;
		boolean again = true;
		while(again){
			System.out.println("Enter number 1: ");
			a = sc.nextInt();
			System.out.println("Enter number 2: ");
			b = sc.nextInt();
			System.out.println(max(a,b));
			System.out.println("Again? 1==yes 0==no");
			again = (sc.nextInt() == 1);
		}
	}

	public static int sign(int num){
		return (num >>> 31) & 1;
	}

	public static int flip(int bit){
		return bit ^ 1;
	}

	public static int max(int a, int b){
		int sign_a = sign(a);
		int sign_b = sign(b);
		
		int use_sign_a = sign_a ^  sign_b;
		int k = sign_a & use_sign_a;
		k ^= ((a-b >>> 31) & 1) & flip(use_sign_a);

		return k*b + (1-k)*a;
	}
}