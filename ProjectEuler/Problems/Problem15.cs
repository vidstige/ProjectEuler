using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler.Problems
{
    class Problem15: ISolvable
    {
        public int ProblemNumber
        {
            get { return 15; }
        }

        private const int Size = 20;

        private long[] _cache = new long[(Size+1) * (Size+1)];

        private long Search(int x, int y)
        {
            int index = x + y * (Size+1);
            if (_cache[index] > 0) return _cache[index];
            if (x == Size && y == Size) return 1;
            
            long result = 0;
            if (x < Size) result += Search(x + 1, y);
            if (y < Size) result += Search(x, y + 1);
            _cache[index] = result;
            return result;
        }

        public string Solve()
        {
            return Search(0, 0).ToString();
        }
    }
}
