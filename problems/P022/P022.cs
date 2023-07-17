namespace Solution
{
    internal class P022
    {
        public void Solution()
        {
            List<int> list1 = new List<int>();
            List<int> list2 = new List<int>();
            Console.WriteLine("Enter the number: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Sum_List(n, list1, list2));
        }
        public string Sum_List(int n, List<int> list1, List<int> list2)
        {
            string[] a = Console.ReadLine().Split(" ");
            while (list1.Count < n)
            { list1.Add(int.Parse(a[list1.Count])); }
            string[] b = Console.ReadLine().Split(" ");
            while (list2.Count < n)
            { list2.Add(int.Parse(b[list2.Count])); }
            List<int> list3 = new List<int>();
            int x = 0;
            while (x < n)
            { 
                var y = list1[x] + list2[x];
                list3.Add(y);
                x++;
            }
            return $"List3 : [{string.Join(", ", list3)}]";
        }
    }
}