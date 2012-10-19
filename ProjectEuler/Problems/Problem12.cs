using System;
using System.Linq;

namespace ProjectEuler.Problems
{
    class Problem12: ISolvable
    {
        public int ProblemNumber { get { return 12; } }
        
        public string Solve()
        {
            int n = 1;
            int triangleNumberN = n;
            int divisors = FactorsOf(triangleNumberN);
            while (divisors < 500)
            {
                //Console.WriteLine("{0}: {1}", triangleNumberN, divisors);
                n++;
                triangleNumberN += n;
                divisors = FactorsOf(triangleNumberN);
            }
            return triangleNumberN.ToString();
        }

        private int FactorsOf(int n)
        {
            return Algorithms.FactorsOf(n).Count();
        }
    }
}
