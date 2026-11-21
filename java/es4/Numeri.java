/*
Esercizio 5

Argomento: rappresentazione dei numeri; divisione intera </> e modulo <%>

Scrivere un programma che

    definisce un numero intero positivo avente al massimo cinque cifre
    visualizza sull'output standard le singole cifre del numero, separandole con uno spazio

Ad esempio, il numero 14356 verrà visualizzato come 1 4 3 5 6. Il numero 367 verrà visualizzato come 0 0 3 6 7. 

Suggerimento: applicare la definizione di notazione posizionale in base 10, studiare le proprietà della divisione intera in Java e del relativo operatore %. Verificare il corretto funzionamento del programma in casi diversi (in particolare, con numeri aventi meno di cinque cifre) e verificare il comportamento del programma in caso di valori di ingresso non ammessi

    numeri con più di cinque cifre
    numeri negativi
    numeri in virgola mobile
    valore di ingresso non numerico (ad esempio: Ciao)

*/

import java.util.Scanner;

public class Numeri {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("Numero: ");
        int n = in.nextInt();

        if (n < 0 || n > 99999) {
            System.out.println("Errore.");
        } else {
            int cifra1 = n / 10000;
            int cifra2 = (n / 1000) % 10;
            int cifra3 = (n / 100) % 10;
            int cifra4 = (n / 10) % 10;
            int cifra5 = n % 10;

            System.out.println(cifra1 + " " + cifra2 + " " + cifra3 + " " + cifra4 + " " + cifra5);
        }

    in.close();
    }
}