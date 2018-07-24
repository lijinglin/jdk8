package testjava;


import java.util.List;
import java.util.ArrayList;
import java.util.Random;

public class AppleFactory 
{
	static Random r = new Random();
	static String [] colors = { "red", "green", "yellow","pink"};
	
	public static int randomInt()
	{
		return Math.abs(r.nextInt()); 
	}
	
	public static String randomColor()
	{
		return colors[ randomInt() % colors.length];
	}
	
	public static int randomWeight()
	{
		return randomInt() % 100;
	}
	
	public static Apple randomApple()
	{
		return new Apple(randomColor(),randomWeight());
	}
	
	
	static List<Apple> buildApples(int n)
	{
		List<Apple> list = new ArrayList<Apple>();
		for(int i = 0; i<n; ++i)
		{
		list.add(randomApple());
		}
		return list;
	}


}