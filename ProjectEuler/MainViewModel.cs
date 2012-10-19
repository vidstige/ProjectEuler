using System;
using System.Collections.ObjectModel;
using System.Linq;
using System.Reflection;
using System.Windows.Threading;
using ProjectEuler.Problems;
using System.Collections.Generic;

namespace ProjectEuler
{
    public class MainViewModel
    {
        private readonly ObservableCollection<ProblemViewModel> _problemSolvers = new ObservableCollection<ProblemViewModel>();

        public ObservableCollection<ProblemViewModel> ProblemSolvers { get { return _problemSolvers; } }

        public void LoadClasses(Dispatcher dispatcher)
        {
            var problemSolvers = new List<ProblemViewModel>();
            Type solvableType = typeof (ISolvable);
            var solvables = Assembly.GetExecutingAssembly().GetTypes().Where(solvableType.IsAssignableFrom);
            foreach (var solvable in solvables.Where(s => !s.IsInterface))
            {
                var instance = (ISolvable) Activator.CreateInstance(solvable);
                problemSolvers.Add(new ProblemViewModel(instance, dispatcher));
            }


            dispatcher.Invoke(() => 
                {
                    foreach (var ps in problemSolvers.OrderBy(ps => ps.ProblemNumber))
                    {
                        _problemSolvers.Add(ps);
                    }
                });
        }
    }
}
