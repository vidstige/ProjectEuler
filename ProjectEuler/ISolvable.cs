namespace ProjectEuler.Problems
{
    public interface ISolvable
    {
        int ProblemNumber { get; }
        string Solve();
    }
}