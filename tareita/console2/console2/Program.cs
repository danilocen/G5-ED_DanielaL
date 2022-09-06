using System;

namespace console2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("OPERACIONES BÁSICAS");
            Console.WriteLine("");

            Console.WriteLine("SUMA DE DOS NUMEROS DEFINIDOS");
            int firstNumber = 12;
            int secondNumber = 7;
            Console.WriteLine(firstNumber + secondNumber);
            Console.WriteLine("");

            Console.WriteLine("SUMA DE PRODUCTOS");
            string firstName = "Bob";
            int carteras = 7;
            Console.WriteLine(firstName + " vendio " + carteras + " carteras.");
            string segundoName = "Juan";
            int bolsas = 7;
            Console.WriteLine(segundoName + " vendio " + bolsas + 7 + " bolsas.");
            string tercerName = "Victor";
            int botellas = 7;
            Console.WriteLine(tercerName + " vendio " + (botellas + 7) + " botellas.");
            Console.WriteLine("");
            Console.WriteLine("OPERACIONES NUMÉRICAS");
            int sum = 7 + 5;
            int difference = 7 - 5;
            int product = 7 * 5;
            int quotient = 7 / 5;
            Console.WriteLine("Suma: " + sum);
            Console.WriteLine("Resta: " + difference);
            Console.WriteLine("Multiplicación: " + product);
            Console.WriteLine("División: " + quotient);
            Console.WriteLine("");

            Console.WriteLine("OPERACIONES CON DECIMALES");
            decimal decimalQuotient = 7.0m / 5;
            Console.WriteLine("Decimal quotient: " + decimalQuotient);

            int first = 7;
            int second = 5;
            decimal division = (decimal)first / (decimal)second;
            Console.WriteLine(division);
            Console.WriteLine("");

            Console.WriteLine("RESTA DE DIVISIÓN");
            Console.WriteLine("Modulus of 200 / 5 : " + (200 % 5));
            Console.WriteLine("Modulus of 7 / 5 : " + (7 % 5));
            Console.WriteLine("");

            Console.WriteLine("ORDEN DE OPERACIONES");
            int value1 = 3 + 4 * 5;
            int value2 = (3 + 4) * 5;
            Console.WriteLine(value1);
            Console.WriteLine(value2);
            Console.WriteLine("");

            Console.WriteLine("INCREMENTO Y DECREMENTO DE VALORES");
            int value = 1;
            value = value + 1;
            Console.WriteLine("First increment: " + value);

            value += 1;
            Console.WriteLine("Second increment: " + value);

            value++;
            Console.WriteLine("Third increment: " + value);

            value = value - 1;
            Console.WriteLine("First decrement: " + value);

            value -= 1;
            Console.WriteLine("Second decrement: " + value);

            value--;
            Console.WriteLine("Third decrement: " + value);
            Console.WriteLine("");

            Console.WriteLine("COLOCACIÓN DE LOS OPERADORES DE INCREMENTO Y DECREMENTO");
            int values = 1;
            values++;
            Console.WriteLine("First: " + values);
            Console.WriteLine("Second: " + values++);
            Console.WriteLine("Third: " + values);
            Console.WriteLine("Fourth: " + (++values));
            Console.WriteLine("");

            Console.WriteLine("DE FAHRENHEIT A CELSIUS");
            int fahrenheit = 94;
            decimal celsius = (fahrenheit - 32m) * (5m / 9m);
            Console.WriteLine("The temperature is " + celsius + " Celsius.");
        }
    }
}
