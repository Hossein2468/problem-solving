namespace Solution
{
    internal class P019
    {
        public void Solution()
        {
            Console.WriteLine("Enter the number: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Pascal_Khayyams_Triangle(n));
        }
        public string Pascal_Khayyams_Triangle(int n)
        {
            List<int> a = new List<int>()
            { 1 };
            List<int> b = new List<int>()
            { 1 , 1 };
            Console.WriteLine(string.Join(", ", a));
            Console.WriteLine(string.Join(", ", b));
            while (a.Count <= n && b.Count <= n)
            {
                if (b.Count <= n)
                {
                    a = new List<int>() { b[0] };
                    int i = 0;
                    while (i < (b.Count - 1))
                    {
                        var x = b[i] + b[i + 1];
                        a.Add(x);
                        i++;
                    }
                    a.Add(b[0]);
                    if (a.Count <= n) { Console.WriteLine(string.Join(", ", a)); }
                }
                if (a.Count <= n)
                {
                    b = new List<int>() { a[0] };
                    int u = 0;
                    while (u < (a.Count - 1))
                    {
                        var y = a[u] + a[u + 1];
                        b.Add(y);
                        u++;
                    }
                    b.Add(a[0]);
                    if (b.Count <= n) { Console.WriteLine(string.Join(", ", b)); }
                }
            }
            return "finish";
        }
    }
}