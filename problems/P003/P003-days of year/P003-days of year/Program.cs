namespace P003_days_of_year
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the first year: ");
            int a = Convert.ToInt32(Console.ReadLine()); 
            Console.WriteLine("Enter the second year: ");
            int b = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine($"there is {Math.Abs((a * 365) - (b * 365))} days between {a} and {b} . ");
        }
    }
}