using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Calculadora
{
    public partial class Form1 : Form
    {
        Numeros nus = new Numeros();
        bool Igual = false;

        public Form1()
        {
            InitializeComponent();
        }
        private void btn1_Click(object sender, EventArgs e)
        {
            txtOperacion.Text += "1";
        }

        private void btn2_Click(object sender, EventArgs e)
        {
            txtOperacion.Text += "2";
        }

        private void btn3_Click(object sender, EventArgs e)
        {
            txtOperacion.Text += "3";
        }

        private void btn4_Click(object sender, EventArgs e)
        {
            txtOperacion.Text += "4";
        }

        private void btn5_Click(object sender, EventArgs e)
        {
            txtOperacion.Text += "5";
        }

        private void btn6_Click(object sender, EventArgs e)
        {
            txtOperacion.Text += "6";
        }

        private void btn7_Click(object sender, EventArgs e)
        {
            txtOperacion.Text += "7";
        }

        private void btn8_Click(object sender, EventArgs e)
        {

            txtOperacion.Text += "8";

        }

        private void btn9_Click(object sender, EventArgs e)
        {
            txtOperacion.Text += "9";
        }

        private void btn0_Click(object sender, EventArgs e)
        {
            txtOperacion.Text += "0";
        }
        private void btnPunto_Click(object sender, EventArgs e)
        {
            txtOperacion.Text += ".";
        }

        private void btnSuma_Click(object sender, EventArgs e)
        {
            if (txtOperacion.Text == "")
            {
                txtOperacion.Text = "";
                return;
            }
            nus.Num = Convert.ToDouble(txtOperacion.Text);
            nus.Opera = "+";
            txtOperacion2.Text += txtOperacion.Text;
            txtOperacion2.Text += nus.Opera;
            txtOperacion.Text = "";
        }

        private void btnResta_Click(object sender, EventArgs e)
        {
            if (txtOperacion.Text == "")
            {
                txtOperacion.Text = "";
                return;
            }
            nus.Num = Convert.ToDouble(txtOperacion.Text);
            nus.Opera = "-";
            txtOperacion2.Text += txtOperacion.Text;
            txtOperacion2.Text += nus.Opera;
            txtOperacion.Text = "";
        }

        private void btnMultiplicacion_Click(object sender, EventArgs e)
        {
            if (txtOperacion.Text == "")
            {
                txtOperacion.Text = "";
                return;
            }
            nus.Num = Convert.ToDouble(txtOperacion.Text);
            nus.Opera = "x";
            txtOperacion2.Text += txtOperacion.Text;
            txtOperacion2.Text += nus.Opera;
            txtOperacion.Text = "";
        }

        private void btnDivision_Click(object sender, EventArgs e)
        {
            if (txtOperacion.Text == "")
            {
                txtOperacion.Text = "";
                return;
            }
            nus.Num = Convert.ToDouble(txtOperacion.Text);
            nus.Opera = "/";
            txtOperacion2.Text += txtOperacion.Text;
            txtOperacion2.Text += nus.Opera;
            txtOperacion.Text = "";

        }
        private void btnPotencia_Click(object sender, EventArgs e)
        {
            if (txtOperacion.Text == "")
            {
                txtOperacion.Text = "";
                return;
            }
            nus.Num = Convert.ToDouble(txtOperacion.Text);
            nus.Opera = "^";
            txtOperacion2.Text += txtOperacion.Text;
            txtOperacion2.Text += nus.Opera;
            txtOperacion.Text = "";

            txtOperacion2.Text += txtOperacion.Text + "^";
            txtOperacion.Text = "";
        }
        private void btnRaiz_Click(object sender, EventArgs e)
        {
            if (txtOperacion.Text == "")
            {
                txtOperacion.Text = "";
                return;
            }
            nus.Num = Convert.ToDouble(txtOperacion.Text);
            nus.Opera = "√";
            txtOperacion2.Text += txtOperacion.Text;
            txtOperacion2.Text += nus.Opera;
            txtOperacion.Text = "";
            txtOperacion.Text = nus.Resultado().ToString();
        }

        private void btnIgual_Click(object sender, EventArgs e)
        {
            if (txtOperacion.Text == "")
            {
                txtOperacion.Text = "";
                return;
            }
            if (Igual == false)
            {
                nus.Num2 = Convert.ToDouble(txtOperacion.Text);
                txtOperacion2.Text += txtOperacion.Text;
                txtOperacion.Text = nus.Resultado().ToString();
            }
        }

        private void btnAC_Click(object sender, EventArgs e)
        {
            if (txtOperacion.Text == "")
            {
                txtOperacion.Text = "";
                return;
            }
            txtOperacion.Clear();
            txtOperacion2.Clear();
            txtOperacion.Focus();
        }

        private void btnDelete_Click(object sender, EventArgs e)
        {
            if (txtOperacion.Text == "")
            {
                txtOperacion.Text = "";
                return;
            }
            txtOperacion.Text = txtOperacion.Text.Remove(txtOperacion.Text.Length - 1);
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.NumPad1)
            {
                txtOperacion.Text += "1";
            }
            if (e.KeyCode == Keys.NumPad2)
            {
                txtOperacion.Text += "2";
            }
            if (e.KeyCode == Keys.NumPad3)
            {
                txtOperacion.Text += "3";
            }
            if (e.KeyCode == Keys.NumPad4)
            {
                txtOperacion.Text += "4";
            }
            if (e.KeyCode == Keys.NumPad5)
            {
                txtOperacion.Text += "5";
            }
            if (e.KeyCode == Keys.NumPad6)
            {
                txtOperacion.Text += "6";
            }
            if (e.KeyCode == Keys.NumPad7)
            {
                txtOperacion.Text += "7";
            }
            if (e.KeyCode == Keys.NumPad8)
            {
                txtOperacion.Text += "8";
            }
            if (e.KeyCode == Keys.NumPad9)
            {
                txtOperacion.Text += "9";
            }
            if (e.KeyCode == Keys.NumPad0)
            {
                txtOperacion.Text += "0";
            }
            if (e.KeyCode == Keys.OemPeriod || e.KeyCode == Keys.Decimal)
            {
                txtOperacion.Text += ".";
            }
            if (e.KeyCode == Keys.Add)
            {
                btnSuma.PerformClick();
            }
            if (e.KeyCode == Keys.Subtract)
            {
                btnResta.PerformClick();
            }
            if (e.KeyCode == Keys.Multiply)
            {
                btnMultiplicacion.PerformClick();
            }
            if (e.KeyCode == Keys.Divide)
            {
                btnDivision.PerformClick();
            }
            if (e.KeyCode == Keys.Enter)
            {
                btnIgual.PerformClick();
            }
            if (e.KeyCode == Keys.Back)
            {
                btnDelete.PerformClick();
            }
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            txtOperacion.Focus();
            this.Focus();
            this.KeyPreview = true;
        }

        
    }

}
