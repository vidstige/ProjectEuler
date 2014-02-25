
using System;
using System.Collections.Generic;
using System.Linq;
namespace ProjectEuler.Problems
{
    class Problem27: ISolvable
    {
        public int ProblemNumber
        {
            get { return 27; }
        }

        private Dictionary<long, bool> _cache = new Dictionary<long, bool>();

        private bool IsPrime(long n)
        {
            if (_cache.ContainsKey(n)) return _cache[n];

            if (n <= 1)
            {
                _cache[n] = false;
                return false;
            }

            for (long i = 2; i < n / 2; i++)
            {
                if (n % i == 0)
                {
                    _cache[n] = false;
                    return false;
                }
            }

            _cache[n] = true;
            return true;
        }

        public string Solve()
        {
            long best = long.MinValue;
            long bestProduct = 0;
            foreach (long a in Enumerable.Range(-1000, 2000))
            {
                foreach (long b in Enumerable.Range(-1000, 2000))
                {
                    long n = 0;
                    while (IsPrime(Math.Abs(n * n) + a * n + b))
                    {
                        n++;
                    }
                    if (n > best)
                    {
                        best = n;
                        bestProduct = a * b;
                        Console.WriteLine("a={0}, b={1}", a, b);
                    }
                }   
            }
            return bestProduct.ToString();
        }
    }
}
