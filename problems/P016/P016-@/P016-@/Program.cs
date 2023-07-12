namespace P016__
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            while (a >= 0)
            {
                int b = 0;
                while(b < a)
                {
                    Console.Write("@");
                    b++;
                }
                Console.WriteLine();
                a--;
            }
        }
    }
}