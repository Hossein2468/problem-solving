namespace P011_fibonacci
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the number: ");
            int n = Convert.ToInt32(Console.ReadLine());
            int a = 1; int b = 1;
            Console.WriteLine(a); Console.WriteLine(b);
            while (a <= n || b <= n)
            { a = a + b;
                if (a <= n) { Console.WriteLine(a); }
                b = b + a; 
                if (b <= n) { Console.WriteLine(b); }
            }
        }
    }
}