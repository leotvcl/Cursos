package business;

public class Customer{
	public String name;
	public Account account;

	public void confirmAccount(){
		System.out.println("Nombre: "+ name);
		System.out.println("Account Number: "+ account.number);
		System.out.println("Accont balance: "+ account.balance);
	}
}