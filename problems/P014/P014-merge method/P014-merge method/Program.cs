namespace P014_merge_method
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<string> list1 = new List<string>();
            List<string> list2 = new List<string>();
            Console.WriteLine("Enter the list1 length: ");
            int n = Convert.ToInt32(Console.ReadLine());
            for (int a = 0; a < n; a++)
            {
                var x = Console.ReadLine();
                list1.Add(x);
            }
            Console.WriteLine("Enter the list2 length: ");
            int m = Convert.ToInt32(Console.ReadLine());
            for (int b = 0; b < m; b++)
            {
                var y = Console.ReadLine();
                list2.Add(y);
            }
            List<string> list3 = new List<string>(); 
            foreach (var c in list1)
            {
                list3.Add(c);
            }
            foreach (var d in list2)
            {
                list3.Add(d);
            }
            Console.WriteLine(string.Join(" , " , list3));
        }
    }
}