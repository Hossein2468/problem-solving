namespace Solution
{
    internal class P005
    {
        public void Solution()
        {
            Console.WriteLine("Enter the first number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter the operator: ");
            string b = Console.ReadLine();
            Console.WriteLine("Enter the second number: ");
            int c = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Operator(a, b, c));
        }
        public int Operator(int a, string b, int c)
        {
            int d = 0;
            if (b == "+") { d = a + c; }
            if (b == "-") { d = a - c; }
            if (b == "*") { d = a * c; }
            if (b == "/") { d = a / c; }
            return d;
        }
    }
}