namespace P004_numbers
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            Dictionary<int, string> numbers = new Dictionary<int, string>()
            {
                {1 , "One" } ,
                {2 , "Two" } ,
                {3 , "Three" } ,
                {4 , "Four" } ,
                {5 , "Five" } ,
                {6 , "Six" } ,
                {7 , "Seven" } ,
                {8 , "Eight" } ,
                {9 , "Nine" } ,
                {10 , "Ten" }
            };
            Console.WriteLine(numbers[a]);
        }
    }
}