// Deafult Constructor

class account {
    private int accId;
    private String name;
    private double balance;

    // Default constructor
    public account(){
        System.out.println("Constructor called...");
    }

    public void showAccount() {
        System.out.println("AccId: " + accId);
        System.out.println("Name: " + name);
        System.out.println("Balance: " + balance);
    }
}

public class defaultConstructor {
    public static void main(String args[]){
        account a = new account();
        a.showAccount();
    }
}
