namespace Solution
{
    internal class P020
    {
        public void Solution()
        {
            Console.WriteLine("Enter the number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Written_Number(a));
        }
        public string Written_Number(int a)
        {
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
            return numbers[a];
        }
    }
}