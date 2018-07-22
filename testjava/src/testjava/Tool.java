package testjava;

import java.util.ArrayList;
import java.util.List;

public	class Tool
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
