namespace P008_factorial
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            int b = 1;
            for (int c = 1; c <= a; c++)
            { b = b * c; }
            Console.WriteLine(b);
        }
    }
}