// Getters and setters

class Product1 {
    private int id;
    private String name;
    private double price;

    public Product1(int i, String nm, double p) {
        id = i;
        name = nm;
        price = p;
    }
    
    public void setName(String nm) {
        name = nm;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }
}
public class gettersAndSetters2 {
    public static void main(String args[]){
        Product1 p = new Product1(101, "Maggi", 35);
        System.out.println("Id: " + p.getId());
        System.out.println("Name: " + p.getName());
        System.out.println("Price: " + p.getPrice());

        System.out.println("After name change");
        p.setName("Atta Maggi");
        System.out.println("Id: " + p.getId());
        System.out.println("Name: " + p.getName());
        System.out.println("Price: " + p.getPrice());
    }
}
