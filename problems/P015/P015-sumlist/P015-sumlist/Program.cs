namespace P015_sumlist
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the number of numbers: ");
            int n = Convert.ToInt32(Console.ReadLine());
            int x = 0;
            for (int a = 0; a < n; a++)
            {
                var m = Convert.ToInt32(Console.ReadLine());
                x = x + m;
            }
            Console.WriteLine(x);
        }
    }
}