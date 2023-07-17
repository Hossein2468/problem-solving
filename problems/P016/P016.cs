namespace Solution
{
    internal class P016
    {
        public void Solution()
        {
            Console.WriteLine("Enter the number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Sign(a));
        }
        public string Sign(int a)
        {
            while (a >= 0)
            {
                int b = 0;
                while (b < a)
                {
                    Console.Write("@");
                    b++;
                }
                Console.WriteLine();
                a--;
            }
            return "finish";
        }
    }
}