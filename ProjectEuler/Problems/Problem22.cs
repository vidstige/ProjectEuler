using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler.Problems
{
    class Problem22: ISolvable, IComparer<string>
    {
        public int ProblemNumber
        {
            get { return 22; }
        }

        private long NameScore(string name)
        {
            int acc = 0;
            foreach (char c in name)
            {
                acc += c - 64;
            }
            return acc;
        }
        
        public string Solve()
        {
            var text = File.ReadAllText(@"C:\Users\vidstige\Downloads\names.txt");
            var names = text.Split(',').Select(s => s.Trim('"')).OrderBy(n => n, this);
            long i = 1;
            long score = 0;
            foreach (var name in names)
            {
                
                if (i == 938)
                {
                    Console.WriteLine("{0}: {1}", name, NameScore(name));
                }

                score += NameScore(name) * i;                
                i++;
            }
            return score.ToString();
        }

        public int Compare(string str1, string str2)
        {
            int i = 0;
            while (i < str1.Length && i < str2.Length)
            {
                if (str1[i] == str2[i])
                {
                    i++;
                }
                else
                {
                    return str1[i] - str2[i];
                }
            }
            return str1.Length - str2.Length;
        }
    }
}
