// Argument Passing

class myMath {
    public void add(int a, int b) {  // a, b are formal arguments / parameters (jaha receive kiya)
        int c = a + b;
        System.out.println("Sum of a + b: " + c);
    }
}
public class argumentPassing1 {
    public static void main(String args[]) {
        myMath m = new myMath();
        int x = 10;
        int y = 10;
        m.add(x, y); // here x, y are actual arguments / arguments (jaha pass kiya)
    }
}
