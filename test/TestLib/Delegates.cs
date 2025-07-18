namespace TestLib
{
    public delegate void DelegateWithNoParametersNoReturn();
    public delegate int DelegateWithNoParametersReturn();
    public delegate void DelegateWithParametersNoReturn(int param0, int param1);
    public delegate int DelegateWithParametersReturn(int param0, int param1);
}
