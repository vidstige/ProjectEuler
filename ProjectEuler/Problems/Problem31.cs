using System.Collections.Generic;
using System.Globalization;
using System.Linq;

namespace ProjectEuler.Problems
{
    class Problem31: ISolvable
    {
        private readonly int [] _coins = new[] { 200, 100, 50, 20, 10, 5, 2, 1 };

        public int ProblemNumber
        {
            get { return 31; }
        }

        private int[] Add(int[] count, int index, int n)
        {
            var result = count.ToArray();
            result[index] += n;
            return result;
        }

        private int SumCoins(IEnumerable<int> count)
        {
            return count.Select((t, i) => _coins[i]*t).Sum();
        }

        private long Search(int pences, int[] count, int start)
        {
            int sum1 = SumCoins(count);
            if (sum1 > pences) return 0;
            if (sum1 == pences) return 1;
            
            long sum = 0;
            for (int i = start; i < _coins.Length; i++)
            {
                sum += Search(pences, Add(count, i, 1), i);
            }
            return sum;
        }

        public string Solve()
        {
            long search = Search(200, new int[_coins.Length], 0);
            return search.ToString(CultureInfo.InvariantCulture);
        }
    }
}
