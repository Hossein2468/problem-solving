namespace P006_sum_numbers
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            int b = 0;
            int c = 0;
            while (b <= a)
            {
                c = c + b;
                b++;
            }
            Console.WriteLine(c); 
        }
    }
}