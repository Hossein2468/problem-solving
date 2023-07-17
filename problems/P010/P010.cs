namespace Solution
{
    internal class P010
    {
        public void Solution()
        {
            Console.WriteLine("Enter the number: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Primorial(n));
        }
        public int Primorial(int n)
        {
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
            return a;
        }
    }
}