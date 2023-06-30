namespace P001_even_odd
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the number : ");
            int a = Convert.ToInt32(Console.ReadLine());
            if (a % 2 == 0)
            {
                Console.WriteLine($"number {a} is even. ");
            }
            else
            {
                Console.WriteLine($"number {a} is odd. ");
            }
        }
    }
}