namespace P018_twin_primes
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the number: ");
            int n = Convert.ToInt32(Console.ReadLine());
            static bool is_prime(int m)
            {
                bool p = true;
                for (int x = 2; x < m; x++)
                {
                    var o = m % x == 0;
                    if (o == true)
                    {
                        p = false;
                        break;
                    }
                }
                return p;
            }
            for (int m = 5; m <= n; m++)
            {
                if (is_prime(m) == true)
                {
                    if (is_prime(m - 2) == true)
                    {
                        Console.Write(m - 2);
                        Console.Write(", ");
                        Console.Write(m);
                        Console.WriteLine();
                    }
                }
            }
        }
    }
}