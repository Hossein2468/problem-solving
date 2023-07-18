namespace Solution
{
    internal class P031
    {
        public void Solution()
        {
            Console.WriteLine("Enter the Number: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Goldbach(n));
            
        }
        public string Goldbach(int n)
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

            static List<int> prime_list(int n)
            {
                List<int> primes = new List<int>();
                for (int m = 2; m < n; m++)
                {
                    if (is_prime(m) == true)
                    {
                        primes.Add(m);
                    }
                }
                return primes;
            }
            static string find_prime(List<int> l, int f)
            {
                foreach (var a in l)
                {
                    foreach (var b in l)
                    {
                        if (a + b == f)
                        {
                            Console.WriteLine($"{a}, {b}");
                        }
                    }
                }
                return "Finish";
            }
            var y = prime_list(n);
            return find_prime(y, n);
        }
    }
}