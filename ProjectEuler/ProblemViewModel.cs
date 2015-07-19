using System;
using System.ComponentModel;
using System.Threading;
using System.Windows.Input;
using System.Windows.Threading;
using ProjectEuler.Problems;

namespace ProjectEuler
{
    public class ProblemViewModel: INotifyPropertyChanged
    {
        private readonly ISolvable _solvable;
        private readonly ICommand _solveProblemCommand;
        private string _answer;

        public ProblemViewModel(ISolvable solvable, Dispatcher dispatcher)
        {
            _solvable = solvable;
            _solveProblemCommand = new SolveProblemCommand(this, dispatcher);
        }

        public string ProblemNumber
        {
            get { return string.Format("Problem {0}", _solvable.ProblemNumber); }
        }

        public ICommand SolveProblem
        {
            get { return _solveProblemCommand; }
        }

        public class SolveProblemCommand : ICommand
        {
            private readonly ProblemViewModel _problemViewModel;
            private readonly Dispatcher _disptacher;

            public SolveProblemCommand(ProblemViewModel problemViewModel, Dispatcher disptacher)
            {
                _problemViewModel = problemViewModel;
                _disptacher = disptacher;
            }

            public bool CanExecute(object parameter)
            {
                return !_problemViewModel.IsSolved;
            }

            public void Execute(object parameter)
            {
                ThreadPool.QueueUserWorkItem(x =>
                    {
                        var answer = _problemViewModel._solvable.Solve();

                        _disptacher.Invoke(() =>
                        {
                            _problemViewModel.Answer = answer;

                            var tmp = CanExecuteChanged;
                            if (tmp != null) tmp(this, EventArgs.Empty);
                        });
                    });
            }

            public event EventHandler CanExecuteChanged;
        }

        public string Answer
        {
            get { return _answer; }
            set
            {
                _answer = value;
                OnPropertyChanged("Answer");
            }
        }

        protected bool IsSolved
        {
            get { return _answer != null; }
        }

        public event PropertyChangedEventHandler PropertyChanged;

        protected virtual void OnPropertyChanged(string propertyName)
        {
            PropertyChangedEventHandler handler = PropertyChanged;
            if (handler != null) handler(this, new PropertyChangedEventArgs(propertyName));
        }
    }
}