using System.Threading;
using System.Windows;

namespace ProjectEuler
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            var viewModel = new MainViewModel();
            ViewModel = viewModel;

            ThreadPool.QueueUserWorkItem(x => viewModel.LoadClasses(Dispatcher));
        }

        protected MainViewModel ViewModel
        {
            set { DataContext = value; }
        }
    }
}