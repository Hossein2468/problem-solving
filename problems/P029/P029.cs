namespace Solution
{
    internal class P029
    {
        public void Solution()
        {
            Console.WriteLine("Enter the numbers: ");
            var m = Console.ReadLine().Split(" ");
            List<int> n = new List<int>();
            foreach (var z in m) { n.Add(int.Parse(z)); }
            Console.WriteLine($"Last 3 numbers are : {Last_Numbers(n)}");
            Console.WriteLine($"2 numbers with highest count are : {Highest_Count(n)}");
            Console.WriteLine($"Max is : {Max(n)}");
            Console.WriteLine($"Min is : {Min(n)}");
            Console.WriteLine($"Average is : {Avg(n)}");
            Console.WriteLine($"Mean is : {Mean(n)}");
            Console.WriteLine($"Sum of all is : {Sum(n)}");
            Console.WriteLine($"Product of all is {Multiply(n)}");
        }
        public int Sum(List<int> n)
        {
            int a = 0;
            foreach (var b in n)
            {
                a += b;
            }
            return a;
        }
        public int Avg(List<int> n)
        {
            var c = n.Count();
            return Sum(n) / c;
        }
        public string Last_Numbers(List<int> n)
        {
            var t = n.Count();
            string a = $"{n[t - 3]}, {n[t - 2]}, {n[t - 1]}";
            return a;
        }
        
        public int Mean(List<int> n)
        {
            n.Sort();
            int h = 0;
            if (n.Count % 2 == 0)
            {
                int b = n.Count / 2;
                h = n[b];
            }
            if (n.Count % 2 != 0)
            {
                int b = n.Count / 2;
                int c = n[b] + n[b + 1];
                h = c / 2;
            }
            return h;
        }
        public int Max(List<int> n)
        {
            n.Sort();
            var r = n.Count();
            return n[r - 1];
        }
        public int Min(List<int> n)
        {
            n.Sort();
            return n[0];
        }
        public string Highest_Count(List<int> n)
        {
            List<int> numbers = new List<int>();
            List<int> Counts = new List<int>();
            foreach (var a in n)
            {
                var b = n.Count(c => c == a );
                Counts.Add(b);
            }
            var c = Counts.IndexOf(Max(Counts));
            numbers.Add(n[c]);
            for (int d = 0; d < Max(Counts); d++)
            {
                Counts[c] = 0;
                c++;
            }
            var e = Counts.IndexOf(Max(Counts));
            numbers.Add(n[e]);
            return $"{numbers[0]} ,{numbers[1]}";
        }
        public Int128 Multiply(List<int> n)
        {
            Int128 a = 1; 
            foreach (Int128 b in n)
            {
                a = a * b;
            }
            return a;
        }
    }
}
