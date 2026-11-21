import java.util.Scanner;

public class IntegerDivider {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("Inserisci m:");
        int m = in.nextInt();

        System.out.println("Inserisci n:");
        int n = in.nextInt();

        int risultato = m / n, resto = m % n;

        System.out.println("Risultato: " + risultato);
        System.out.println("Resto: " + resto);
    }
}