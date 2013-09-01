
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
namespace ProjectEuler.Problems
{
    class Problem26: ISolvable
    {
        public int ProblemNumber { get { return 26; } }

        public string Solve()
        {
            int max = 0;
            int maxRecuring = -1;
            foreach (int d in Enumerable.Range(2, 999))
            {
                int recuring = RecuringLength(d);
                //Console.WriteLine("{0}: {1}", d, recuring);
                if (recuring > maxRecuring)
                {
                    Console.WriteLine("{0}: {1}", d, recuring);
                    max = d;
                    maxRecuring = recuring;
                }
            }
            return max.ToString(); 

            //return RecuringLength(37).ToString();
        }

        private int RecuringLength(int d)
        {
            int i = 1;

            var memory = new List<int>();
            while (i > 0 && !memory.Contains(i))
            {
                memory.Add(i);
                i = i * 10;
                i = i % d;
            }

            if (i == 0) return 0;
            return memory.Count - memory.IndexOf(i);
        }
        
        private string Recuring(int d)
        {
            int i = 1;

            var memory = new List<int>();
            var s = new StringBuilder();
            while (i > 0 && !memory.Contains(i))
            {
                memory.Add(i);
                i = i * 10;
                s.Append(i / d);
                i = i % d;
            }

            var t = s.ToString();
            if (i == 0) return "0." + t;
            var idx = memory.IndexOf(i);
            return "0." + t.Substring(0, idx) + "(" + t.Substring(idx) + ")";
        }
    }
}
