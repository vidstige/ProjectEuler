using System;

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
            int result = 0;
            for (int i=2; i < Math.Sqrt(n); i++)
            {
                if (n % i == 0) result+=2;
            }
            return result;
        }
    }
}
