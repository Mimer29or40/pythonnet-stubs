namespace TestLib;

public interface IBasic;

public interface IGeneric<TA, TB>;

public interface IInterfaces : IComparable<object>, IEquatable<object>;

public interface IFields { public static int A = 0; public static int B = 0; }

public interface IProperties { public int A { get; } public int B { get; set; } }

public interface IMethods { public void A(); public int B(); }

public interface IDunderMethods
{
    public static IDunderMethods operator +(IDunderMethods self) => self;
    public static IDunderMethods operator -(IDunderMethods self) => self;
    public static IDunderMethods operator ++(IDunderMethods self) => self;
    public static IDunderMethods operator --(IDunderMethods self) => self;
    public static IDunderMethods operator +(IDunderMethods left, IDunderMethods right) => left;
    public static IDunderMethods operator -(IDunderMethods left, IDunderMethods right) => left;
    public static IDunderMethods operator *(IDunderMethods left, IDunderMethods right) => left;
    public static IDunderMethods operator /(IDunderMethods left, IDunderMethods right) => left;
    public static IDunderMethods operator %(IDunderMethods left, IDunderMethods right) => left;
    public static IDunderMethods operator ~(IDunderMethods self) => self;
    public static IDunderMethods operator &(IDunderMethods left, IDunderMethods right) => left;
    public static IDunderMethods operator |(IDunderMethods left, IDunderMethods right) => left;
    public static IDunderMethods operator ^(IDunderMethods left, IDunderMethods right) => left;
    public static IDunderMethods operator <<(IDunderMethods left, IDunderMethods right) => left;
    public static IDunderMethods operator >>>(IDunderMethods left, IDunderMethods right) => left;
    public static bool operator !(IDunderMethods self) => true;
    public static bool operator true(IDunderMethods self) => true;
    public static bool operator false(IDunderMethods self) => false;
    // public static bool operator ==(IDunderMethods left, IDunderMethods right) => true;
    // public static bool operator !=(IDunderMethods left, IDunderMethods right) => true;
    public static bool operator <(IDunderMethods left, IDunderMethods right) => true;
    public static bool operator <=(IDunderMethods left, IDunderMethods right) => true;
    public static bool operator >(IDunderMethods left, IDunderMethods right) => true;
    public static bool operator >=(IDunderMethods left, IDunderMethods right) => true;
}

public interface IListMethods : IList<int>;

public interface IEvents { public event EventHandler A; public event EventHandler<EventArgs> B; }

public interface INested
{
    public class NestedClass;
    public struct NestedStruct;
    public record NestedRecord;
    public interface INested;
    public enum NestedEnum;
    public delegate void NestedDelegate();
}