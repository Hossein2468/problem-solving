namespace Solution
{
    internal class P007
    {
        public void Solution()
        {
            Console.WriteLine("Enter the number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Number(a));
        }
        public int Number(int a)
        {
            for (int b = 0; b <= a; b = b + 5)
            { if (b > 1) { return b; } }
            return 0;
        }
    }
}