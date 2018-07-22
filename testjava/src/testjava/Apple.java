package testjava;

public class Apple
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