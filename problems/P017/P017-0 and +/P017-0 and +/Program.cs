namespace P017_0_and__
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the number: ");
            int n = Convert.ToInt32(Console.ReadLine());
            int i = n;
            while (n >= 0)
            {
                int a = 0;
                while (a < n)
                {
                    Console.Write("+");
                    a++;
                }
                int h = i - n;
                while (h > 0)
                {
                    Console.Write("0");
                    h--;
                }
                Console.WriteLine();
                n--;
            }
        }
    }
}