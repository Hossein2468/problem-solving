namespace P002_function
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the first number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter the second number: ");
            int b = Convert.ToInt32(Console.ReadLine()); 
            static int sum(int x , int y) { return x + y; } 
            static int subtract(int x , int y) { return x - y; }
            static int multiply(int x , int y) { return x * y; }
            static double divide(double x , double y) { return x / y; }
            Console.WriteLine($"sum of numbers is {sum(a, b)}");
            Console.WriteLine($"subtract of numbers is {subtract(a, b)}");
            Console.WriteLine($"multiply of numbers is {multiply(a, b)}");
            Console.WriteLine($"divide of numbers is {divide(a, b)}");
        }
    }
}