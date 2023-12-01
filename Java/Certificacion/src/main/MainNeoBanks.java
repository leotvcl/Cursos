package main;
import javax.swing.JOptionPane;
import business.Account;
import business.Customer;

public class MainNeoBanks{

	public static void main(String params[]){
		Account account = new Account();
		//account.number = "13246740";
		account.number = JOptionPane.showInputDialog("Ingrese Número de cuenta: ");
		account.balance = 1_000_000d;

		Customer leonardo = new Customer();
		//leonardo.name = "Leonardo";
		leonardo.name = JOptionPane.showInputDialog("Ingrese nombre: ");
		leonardo.account = account;
		leonardo.confirmAccount();
	}
}