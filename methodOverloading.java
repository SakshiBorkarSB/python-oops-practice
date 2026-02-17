// Method Overloading

class Addition {
    public int Add (int a, int b) {
        int c = a + b;
        return c;
    }

    public int Add (int a, int b, int c) {
        int d = a + b + c;
        return d;
    }
    
    public double Add (double i, double j) {
        double k = i + j;
        return k;
    }

    public String Add (String s1, String s2) {
        String s3 = s1 + s2;
        return s3;
    }

    public void Show(int age, String name) {
        System.out.println("Age: " + age);
        System.out.println("Name: " + name);
    }

    public void Show(String name, int age) {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

public class methodOverloading {
    public static void main(String args[]) {
        Addition a = new Addition();
        System.out.println("Addition of 10 and 20: " + a.Add(10, 20));
        System.out.println("Addition of 10 and 20 and 30: " + a.Add(10, 20, 30));
        System.out.println("Addition of 10.5 and 20.5: " + a.Add(10.5, 20.5));
        System.out.println("Addition of Hi and Sakshi: " + a.Add("Hi ", "Sakshi!"));
        a.Show(21, "Sakshi");
        a.Show("Sakshi", 21);
    }
}
