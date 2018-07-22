package testjava;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.*;
import java.util.function.*;

interface  Format<T>
{
	public void  test(T t);
}

interface  Match<T>
{
	boolean test(T t);
}

class Apple
{
	Apple(String color,int weight)
	{
		this.color = color;
		this.weight = weight;
	}

	public int getWeight() {
		return weight;
	}
	public void setWeight(int weight) {
		this.weight = weight;
	}
	private String color;
	public String getColor() {
		return color;
	}

	public void setColor(String color) {
		this.color = color;
	}
	int weight;
	
	public String toString()
	{
		return "Apple[color=" + getColor() + ",weight=" + getWeight() + "]";
	}

}

class Tool
{
	static public  <T> List<T> filter(List<T> inventory , Match<T> match)
	{
		List<T> retList = new ArrayList<T>();
		for(T t: inventory)
		{
			if(match.test(t)) retList.add(t);
		}
		return retList;
	}
	
	static <T> void outputList(List<T> list, Format<T> f)
	{
		for(T e: list)
		{
			f.test(e);
		}
	}
	
	static List<Apple> buildAppleList()
	{
		List<Apple> list = new ArrayList<Apple>();
		list.add(new Apple("red",30));
		list.add(new Apple("yellow",50));
		list.add(new Apple("red",40));
		list.add(new Apple("green",30));
		list.add(new Apple("red",35));
		list.add(new Apple("red",44));
		list.add(new Apple("green",36));
		list.add(new Apple("red",32));
		
		return list;
	}
	
	
	
	
}

public class Main {

	static void log(Object str)
	{
		if(str == null)
			System.out.println("null");
		else
			System.out.println(str.toString());
	}
	
	static void testApple()
	{
		List<Apple> inventory = Tool.buildAppleList();
		List<Apple> retList = Tool.filter(inventory,(Apple e)->{return e.weight > 32;});
		Tool.outputList(retList,(Apple e)->{ System.out.println(e.getColor());});
		Consumer<Apple> c =  (Apple e)->{System.out.println(e.getColor() + ":" + e.getWeight());};
		inventory.stream().filter((Apple e)->{return e.weight > 32;}).forEach(System.out::println);
		
		inventory.stream().map(Apple::getWeight).forEach(System.out::println);
		//inventory.stream().sort((Apple left,Apple right)->(left.getWeight() - right.getWeight())).limit(3).forEach(System.out::println);
		System.out.println("colors:");
		inventory.stream().map(Apple::getColor).distinct().forEach(System.out::println);
		log("flatmap:");
		inventory.stream().map(Apple::getColor).distinct().map(s->s.split("")).flatMap(Arrays::stream).forEach(Main::log);
		boolean match = inventory.stream().anyMatch((Apple a)->{log("anymatch:" + a); return a.getColor().equals("red") && a.getWeight()>40;});
		if(match) log("match");
		int sum = inventory.stream().map(Apple::getWeight).reduce(0,Integer::sum);
		log("sum=" + sum);
		log("weight");
		inventory.stream().map(Apple::getWeight).sorted((Integer left,Integer right)->right-left).limit(5).forEach(System.out::println);
	}
	
	public static void testXyz()
	{
		int [] cc = new int[] {2,3};
		IntStream range1 = IntStream.rangeClosed(1,100);

		Stream stream = range1.boxed().flatMap((x)->  IntStream.rangeClosed(x,100).filter((y)-> Math.sqrt(x*x + y * y) % 1 == 0).mapToObj((y)-> new int[] {x,y}));
		stream.forEach((e)->{int[] x = (int [] ) e;log("" + x[0] + "," + x[1]);});
	}
	
	static void testFibonacci()
	{
		Stream<int[]> stream = Stream.iterate(new int[] {0,1},(t)->(new int[] {t[1],t[0] + t[1]}));
		stream.limit(20).forEach(t->System.out.println(t[0] + "," + t[1]));
	}
	
	static void testFile()
	{
		try {
			Stream<String> lineStream =Files.lines(Paths.get("d:/log_network.txt"), Charset.defaultCharset());
			Stream<String> wordStream = lineStream.flatMap(x->Arrays.stream(x.split("\\s")));
			wordStream.distinct().forEach(System.out::println);
			//log(wordStream.distinct().count());
		}
		catch(IOException ex)
		{
			ex.printStackTrace();
		}
	}
	public static void main(String[] args)
	{
		testFile();
		//stream.filter((int [] arr)->sqrt(arr[0] * arr[0] + arr[1]*arr[1]) %1 == 0 ).forEach((arr)->System.out.println(arr[0] +"," + arr[1]));
	} 
	
	
}
