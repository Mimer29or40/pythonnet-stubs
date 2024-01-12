namespace TestLib
{
    public delegate void DelegateWithNoParmetersNoReturn();
    public delegate int DelegateWithNoParmetersReturn();
    public delegate void DelegateWithParmetersNoReturn(int param0, int param1);
    public delegate int DelegateWithParmetersReturn(int param0, int param1);
}
