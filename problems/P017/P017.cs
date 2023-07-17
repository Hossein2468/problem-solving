namespace Solution
{
    internal class P017
    {
        public void Solution()
        {
            Console.WriteLine("Enter the number: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Signs(n));
        }
        public string Signs(int n)
        {
            int i = n;
            while (n >= 0)
            {
                int a = 0;
                while (a < n)
                {
                    Console.Write("+");
                    a++;
                }
                int h = i - n;
                while (h > 0)
                {
                    Console.Write("0");
                    h--;
                }
                Console.WriteLine();
                n--;
            }
            return "finish";
        }
    }
}