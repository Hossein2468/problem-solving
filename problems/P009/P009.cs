namespace Solution
{
    internal class P009
    {
        public void Solution()
        {
            Console.WriteLine("Enter the number: ");
            int n = Convert.ToInt32(Console.ReadLine());
        }
        public int Prime_Number(int n)
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
            for (int m = 2; m <= n; m++)
            {
                if (isprime(m))
                { return m; }
            }
            return 0;
        }
    }
}