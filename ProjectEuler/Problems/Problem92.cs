using System.Collections.Generic;
using System.Linq;

namespace ProjectEuler.Problems
{
    class Problem92: ISolvable
    {
        public int ProblemNumber
        {
            get { return 92; }
        }

        private IEnumerable<int> Digits(long i)
        {
            while (i > 0)
            {
                var digit = (int)(i%10);
                i = i / 10;
                yield return digit;
            }
        }

        private int FindLoop(int i)
        {
            while (i != 89 && i != 1)
            {
                i = Digits(i).Select(x => x*x).Sum();
            }
            return i;
        }

        public string Solve()
        {
            int count = 0;
            for (int i = 1; i < 10000000; i++)
            {
                var l = FindLoop(i);
                if (l == 89) count++;
            }
            return count.ToString();
        }
    }
}
