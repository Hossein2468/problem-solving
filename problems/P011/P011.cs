namespace Solution
{
    internal class P011
    {
        public void Solution()
        {
            Console.WriteLine("Enter the number: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Fibonacci(n));
        }
        public int Fibonacci(int n)
        {
            int a = 1; int b = 1;
            Console.WriteLine(a); Console.WriteLine(b);
            while (a <= n || b <= n)
            {
                a = a + b;
                if (a <= n) { return a; }
                b = b + a;
                if (b <= n) { return b; }
            }
            return 0;
        }
    }
}