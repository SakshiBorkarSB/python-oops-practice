// Encapsulation

class Student1{
    private int rollno;
    private String name;
    private double per;

    // method to initialise - setter
    public void setStudent(int r, String n, double p){ // for s (-101, "Sara", 95)
    // agar yeh method nahi hota tohhum rollno wali condition nahi laga paate and main directly negative rollno ko access kr leta
        if ( r < 0) {
            System.out.println("Roll number cannot be negaive");
        }
        else {
            rollno = r;
        }
        name = n;
        per = p;
    }

    // method to display
    public void showStudent(){
        System.out.println("Rollno: " + rollno);
        System.out.println("Name: " + name);
        System.out.println("Percentage: " + per);
    }
}

public class encapsulation{
    public static void main(String args[]){
        Student1 s;
        s = new Student1();
        s.setStudent(-101, "Sara", 95);
        s.showStudent();

        Student1 r = new Student1();
        r.setStudent(102, "Riya", 94);
        r.showStudent();
    }
}
