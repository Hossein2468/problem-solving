namespace Solution
{
    internal class P034
    {
        public void Solution()
        {
            Console.WriteLine("Enter the number: ");
            int n = Convert.ToInt32(Console.ReadLine());
            var r = Numbers(n);
            Console.WriteLine(Is_Prime(r));
        }
        public List<int> Numbers(int n)
        {
            List<int> numbers1 = new List<int>();
            var a = n.ToString();
            var b = 0; 
            while (b < a.Length)
            {
                for (int c = b + 1; c < a.Length + 1; c++)
                {
                    var d = a[b..c];
                    if (d != "0" && d != "1")
                    {
                        numbers1.Add(int.Parse(d));
                    }
                }
                b++;
            }
            var i = numbers1.ToHashSet();
            List<int> numbers = new List<int>(i);
            return numbers;
        }
        public string Is_Prime(List<int> r)
        {
            HashSet<int> myset = new HashSet<int>();
            foreach (var a in r)
            {
                for (int x = 2; x < a; x++)
                {
                    if (a % x == 0)
                    {
                        myset.Add(a);
                    }
                }
            }
            foreach (var i in myset)
            {
                r.Remove(i);
            }
            var h = r.ToHashSet();
            return string.Join(", ", h);
        }
    }
}
