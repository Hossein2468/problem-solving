namespace P005_numbers_and_operators
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the first number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter the operator: ");
            string b = Console.ReadLine();
            Console.WriteLine("Enter the second number: ");
            int c = Convert.ToInt32(Console.ReadLine());

            if (b == "+") { Console.WriteLine(a + c); }
            if (b == "-") { Console.WriteLine(a - c); }
            if (b == "*") { Console.WriteLine(a * c); }
            if (b == "/") { Console.WriteLine(a / c); }
        }
    }
}