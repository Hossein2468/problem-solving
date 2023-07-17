namespace Solution
{
    internal class P006
    {
        public void Solution()
        {
            Console.WriteLine("Enter the number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Sum(a)); 
        }
        public int Sum(int a)
        {
            int b = 0;
            int c = 0;
            while (b <= a)
            {
                c = c + b;
                b++;
            }
            return c; 
        }
    }
}