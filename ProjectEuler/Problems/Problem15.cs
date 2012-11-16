using System;

namespace ProjectEuler.Problems
{
    class Problem15: ISolvable
    {
        public int ProblemNumber { get { return 15; } }
        private const int Size = 20;

        private int Search(int x, int y)
        {
            if (x == Size && y == Size) return 1;

            int routes = 0;
            if (x < Size) routes += Search(x+1, y);
            if (y < Size) routes += Search(x, y+1);
            return routes;
        }

        public string Solve()
        {
            return Search(0, 0).ToString();
        }
    }
}
