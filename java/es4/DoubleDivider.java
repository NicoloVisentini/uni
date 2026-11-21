import java.util.Scanner;

public class DoubleDivider {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("Inserisci m:");
        double m = in.nextDouble();

        System.out.println("Inserisci n:");
        double n = in.nextDouble();

        double risultato = m / n, resto = m % n;

        System.out.println("Risultato: " + risultato);
        System.out.println("Resto: " + resto);
    }
}