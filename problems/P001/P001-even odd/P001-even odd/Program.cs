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
                Console.Write("number ");
                Console.Write(a);
                Console.Write(" is even.");
            }
            else
            {
                Console.Write("number ");
                Console.Write(a);
                Console.Write(" is odd. ");
            }
        }
    }
}