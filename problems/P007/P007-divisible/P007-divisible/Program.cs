namespace P007_divisible
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            for (int b = 0; b <= a; b = b + 5)
            { if (b > 1) { Console.WriteLine(b); } } 
        }
    }
}