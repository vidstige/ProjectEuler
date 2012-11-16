using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler.Problems
{
    class Problem21: ISolvable
    {
        public int ProblemNumber
        {
            get { return 21; }
        }

        private int[] _cache = new int[10000];
        private int d(int n)
        {
            if (_cache[n] > 0) return _cache[n];
            int tmp = Algorithms.FactorsOf(n).Sum() + 1;
            _cache[n] = tmp;
            return tmp;
        }

        public string Solve()
        {
            var amicable = new HashSet<int>();
            for (int a = 2; a < 10000; a++)
            {
                for (int b = 2; b < 10000; b++)
                {
                    if (a != b)
                    {
                        if (d(a) == b && d(b) == a)
                        {
                            amicable.Add(a);
                            amicable.Add(b);
                        }
                    }
                }
            }

            return amicable.Sum().ToString();
        }
    }
}
