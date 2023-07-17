namespace Solution
{
    internal class P008
    {
        public void Solution()
        {
            Console.WriteLine("Enter the number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Factorial(a));
        }
        public int Factorial(int a)
        {
            int b = 1;
            for (int c = 1; c <= a; c++)
            { b = b * c; }
            return b;
        }
    }
}