namespace P012_prime_numbers
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the number: ");
            int n = Convert.ToInt32(Console.ReadLine()); 
            static bool is_prime(int m)
            { bool p = true; 
            for (int x = 2; x < m; x++)
                { var o = m % x == 0;
                if (o == true)
                    { p = false;
                        break;
                    }
                }
                return p;
            }
            int a = 0;
            int u = 2; 
            while (a <= n)
            { if (is_prime(u) == true)
                { a++;
                    if (a == n)
                    { Console.WriteLine(u); }
                }
                u++;
            }
        }
    }
}