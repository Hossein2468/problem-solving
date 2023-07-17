namespace Solution
{
    internal class P003
    {
        public void Solution()
        {
            Console.WriteLine("Enter the first year: ");
            int a = Convert.ToInt32(Console.ReadLine()); 
            Console.WriteLine("Enter the second year: ");
            int b = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Days_Of_Year(a, b));
        }
        public string Days_Of_Year(int a, int b)
        {
            return $"there is {Math.Abs((a * 365) - (b * 365))} days between {a} and {b} . ";
        }
    }
}