namespace Solution
{
    internal class P002
    {
         public void Solution()
        {
            Console.WriteLine("Enter the first number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter the second number: ");
            int b = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Methods(a, b));
        }
        public string Methods(int a, int b)
        {
            static int sum(int x, int y) { return x + y; }
            static int subtract(int x, int y) { return x - y; }
            static int multiply(int x, int y) { return x * y; }
            static double divide(double x, double y) { return x / y; }
            return @$"sum of numbers is {sum(a, b)}
            subtract of numbers is {subtract(a, b)}
            multiply of numbers is {multiply(a, b)}
            divide of numbers is {divide(a, b)}";
        }
    }
}