namespace Solution
{
    internal class P015
    {
        public void Solution()
        {
            Console.WriteLine("Enter the number of numbers: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Sum_List(n));
        }
        public int Sum_List(int n)
        {
            int x = 0;
            for (int a = 0; a < n; a++)
            {
                var m = Convert.ToInt32(Console.ReadLine());
                x = x + m;
            }
            return x;
        }
    }
}