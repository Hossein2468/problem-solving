namespace Solution
{
    internal class P001
    {
        public void Solution()
        {
            Console.WriteLine("Enter the number : ");
            int a = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Even_Odd(a));
            
        }
        public string Even_Odd(int a)
        {
            if (a % 2 == 0)
            {
                return $"number {a} is even. ";
            }
            else
            {
                return $"number {a} is odd. ";
            }
        }
    }
}