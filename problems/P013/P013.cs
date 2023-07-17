using System.Diagnostics.Tracing;

namespace Solution
{
    internal class P013
    {
        public void Solution()
        {
            Console.WriteLine("Enter the number: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Prime_Factors(n));
        }
        public int Prime_Factors(int n)
        {
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
            List<int> prime_numbers = new List<int>();
            for (int m = 2; m < n; m++)
            {
                if (is_prime(m) == true)
                { prime_numbers.Add(m); }
            }
            List<int> prime_factors = new List<int>();
            foreach (var i in prime_numbers)
            {
                while (n % i == 0)
                {
                    n = n / i;
                    prime_factors.Add(i);
                    if (n == 1)
                    { break; }
                }
            }
            foreach (var a in prime_factors)
            { return a; }
            return 0;
        }
    }
}