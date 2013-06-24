using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler.Problems
{
    class Problem23 : ISolvable
    {
        public int ProblemNumber
        {
            get { return 23; }
        }

        private Dictionary<int, bool> _abundantCache = new Dictionary<int, bool>();
        private bool IsAbundant(int n)
        {
            bool val;
            if (_abundantCache.TryGetValue(n, out val))
            {
                return val;
            }

            long sum = 0;
            for (int i = 1; i < n; i++) if (n % i == 0) sum += i;

            _abundantCache[n] = sum > n;

            return sum > n;
        }

        private IList<int> _abundant = new List<int>();

        private bool IsAbundantSum(int n)
        {
            foreach (int x in _abundant)
                foreach (int y in _abundant)
                {
                    if (x + y == n) return true;
                }
            return false;
        }

        public string Solve()
        {
            for (int i = 1; i < 28123; i++)
            {
                if (IsAbundant(i)) _abundant.Add(i);
            }

            long sum = 0;
            for (int i = 1; i < 28123; i++)
            {
                if (!IsAbundantSum(i)) sum += i;
            }

            return sum.ToString();
        }
    }
}