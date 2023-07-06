namespace P010_primorial
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the number: ");
            int n = Convert.ToInt32(Console.ReadLine());
            static bool isprime(int m)
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
                int a = 1;
                for (int m = 2; m <= n; m++)
                {
                    if (isprime(m) == true)
                    { a = m * a; }
                }
                Console.WriteLine(a);
        }
    }
}