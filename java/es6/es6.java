/*
Esercizio 6

Argomento: rappresentazione dei numeri; divisione intera </> e modulo <%>

Scrivere un programma che definisca un numero razionale positivo n nell'
intervallo [0, 32) e ne stampi a standard output la codifica binaria in 
formato a virgola fissa, usando cinque cifre binarie per la parte intera
e cinque per quella frazionaria. Esempio: 8.5 in base dieci = 01000.10000
in base due.
Suggerimento: si usino gli algoritmi di conversione da decimale a binario
della parte intera e della parte frazionaria presentati a lezione.
*/

import java.util.Scanner;

public class es6 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("Numero (0-32): ");
        double numero = in.nextDouble();

        if (numero < 0 || numero >= 32) {
            System.out.println("Errore.");
        } else {

            // Separazione della parte intera e frazionaria
            int intero = (int) numero;
            double decimale = numero - intero;

            // Conversione della parte intera
            String binarioIntero = "";

            for (int i = 0; i < 5; i++) {
                int resto = intero % 2;
                binarioIntero = resto + binarioIntero;
                intero = intero / 2;
            }

            // Conversione della parte frazionaria
            String binarioDecimale = "";

            for (int i = 0; i < 5; i++) {
                decimale = decimale * 2;

                if (decimale >= 1) {
                    binarioDecimale = binarioDecimale + "1";
                    decimale = decimale - 1;
                } else {
                    binarioDecimale = binarioDecimale + "0";
                }
            }

            // Stampa del risultato
            System.out.println(binarioIntero + "." + binarioDecimale);
        }

        in.close();
    }
}