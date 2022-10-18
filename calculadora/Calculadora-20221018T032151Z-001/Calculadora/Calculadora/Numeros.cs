using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Calculadora
{
    class Numeros
    {
        public double num;
        public double Num { set; get; }
        public double Num2 { set; get; }
        public string Opera { set; get; }
        public Numeros()
        {
            Num = 0;
            Num2 = 0;
        }
        public double Resultado()
        {
            double txtOperacion = 0;

            switch (Opera)
            {
                case "+":
                    txtOperacion = (Num2 + Num);
                    break;

                case "-":
                    txtOperacion = (Num - Num2);
                    break;

                case "x":
                    txtOperacion = (Num2 * Num);
                    break;

                case "/":
                    txtOperacion = (Num2 / Num);
                    break;
                case "^":
                    txtOperacion = Math.Pow(Num, Num2);
                    break;
                case "√":
                    txtOperacion = Math.Sqrt(Num2);
                    break;
            }
            return txtOperacion;
        }
    }
}
