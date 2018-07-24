package testjava;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.*;
import java.util.function.*;
import java.util.stream.Collectors;

interface  Format<T>
{
	public void  test(T t);
}

interface  Match<T>
{
	boolean test(T t);
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
	
	static void testGenerateNum()
	{
		Stream.generate(Math::random).limit(100).forEach(System.out::println);
	}
	
	static void testGenerateApple()
	{
		Stream.generate(()->AppleFactory.randomApple()).limit(20).forEach(System.out::println);
	}
	
	public static HashMap<String,Integer> accumulate(Apple apple)
	{
		HashMap<String,Integer>map = new HashMap<String,Integer>();
		map.put(apple.getColor(),apple.getWeight());
		log("accumulate" + apple);

		return map;
	}
	
	static public HashMap<String,Integer> accumulateMap(HashMap<String,Integer>left, HashMap<String,Integer> right)
	{
		for(Map.Entry<String, Integer> entry : left.entrySet())
		{
			Integer rightValue = right.get(entry.getKey());
			if(rightValue != null)
				{
					entry.setValue(entry.getValue() + rightValue);
					right.remove(entry.getKey());
				}
		}
		
		left.putAll(right);
		return left;
	}
	
	public static void main(String[] args)
	{
		//testFile();
		
		//testGenerateNum();
		testGenerateApple();
		int sum = AppleFactory.buildAppleStream(20).collect(Collectors.reducing(0,Apple::getWeight,(left,right)->left>right?left:right));
		log("max =" + sum);
		HashMap map = AppleFactory.buildAppleStream(20).collect(Collectors.reducing(new HashMap<String,Integer>(),Main::accumulate,Main::accumulateMap));
		log("reducing result:" + map);
		String joinStr = AppleFactory.buildAppleStream(20).map(Apple::getColor).collect(Collectors.joining(","));
		log(joinStr);
		
		int result = AppleFactory.buildAppleStream(20).collect(Collectors.reducing(0,t->t.getWeight(),Integer::sum));
		log(result);
		result = AppleFactory.buildAppleStream(20).reduce(0,(val,t)->val + 1,(left,right)->left + right);
		log(result);
		//stream.filter((int [] arr)->sqrt(arr[0] * arr[0] + arr[1]*arr[1]) %1 == 0 ).forEach((arr)->System.out.println(arr[0] +"," + arr[1]));
	} 
	
	
}
