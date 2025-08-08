namespace TestLib;

public delegate void DelegateBasic();

public delegate void DelegateParameters(int param0, int param1);

public delegate int DelegateReturn();

public delegate T DelegateGeneric<out T, in T0, in T1>(Enum param0, T1 param1);