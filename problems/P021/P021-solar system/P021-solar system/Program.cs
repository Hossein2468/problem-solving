namespace P021_solar_system
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, int> solar_system = new Dictionary<string, int>()
            {
                { "Mercry", 58 },
                { "Venus", 120 },
                { "Earth", 180 },
                { "Mars", 250 },
                { "Jupiter", 777 },
                { "Saturn", 1430 },
                { "Uranus", 2880 },
                { "Neptune", 4500 }
            };
            foreach (KeyValuePair<string, int> a in solar_system)
            {
                int b = a.Value / 58;
                string c = new string('-', b);
                Console.WriteLine($"sun {c} {a.Key}");
            }
        }
    }
}