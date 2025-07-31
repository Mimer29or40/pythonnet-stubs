using System.Collections;

namespace TestLib;

public struct StructBasic;

public struct StructGeneric<TA, TB>;

public struct StructInterfaces : IComparable<object>, IEquatable<object>
{
    public int CompareTo(object? other) { throw new NotImplementedException(); }
}

public struct StructFields { public StructFields() { } public int A = 0; public int B = 0; }

public struct StructConstructors
{
    public StructConstructors() { }
    public StructConstructors(int param0, int param1) { }
}

public struct StructProperties { public int A { get; } public int B { get; set; } }

public struct StructMethods { public void A() { } public int B() { return 0; } }

public struct StructDunderMethods
{
    public static StructDunderMethods operator +(StructDunderMethods self) => self;
    public static StructDunderMethods operator -(StructDunderMethods self) => self;
    public static StructDunderMethods operator ++(StructDunderMethods self) => self;
    public static StructDunderMethods operator --(StructDunderMethods self) => self;
    public static StructDunderMethods operator +(StructDunderMethods left, StructDunderMethods right) => left;
    public static StructDunderMethods operator -(StructDunderMethods left, StructDunderMethods right) => left;
    public static StructDunderMethods operator *(StructDunderMethods left, StructDunderMethods right) => left;
    public static StructDunderMethods operator /(StructDunderMethods left, StructDunderMethods right) => left;
    public static StructDunderMethods operator %(StructDunderMethods left, StructDunderMethods right) => left;
    public static StructDunderMethods operator ~(StructDunderMethods self) => self;
    public static StructDunderMethods operator &(StructDunderMethods left, StructDunderMethods right) => left;
    public static StructDunderMethods operator |(StructDunderMethods left, StructDunderMethods right) => left;
    public static StructDunderMethods operator ^(StructDunderMethods left, StructDunderMethods right) => left;
    public static StructDunderMethods operator <<(StructDunderMethods left, StructDunderMethods right) => left;
    public static StructDunderMethods operator >>>(StructDunderMethods left, StructDunderMethods right) => left;
    public static bool operator !(StructDunderMethods self) => true;
    public static bool operator true(StructDunderMethods self) => true;
    public static bool operator false(StructDunderMethods self) => false;
    public static bool operator ==(StructDunderMethods left, StructDunderMethods right) => true;
    public static bool operator !=(StructDunderMethods left, StructDunderMethods right) => true;
    public static bool operator <(StructDunderMethods left, StructDunderMethods right) => true;
    public static bool operator <=(StructDunderMethods left, StructDunderMethods right) => true;
    public static bool operator >(StructDunderMethods left, StructDunderMethods right) => true;
    public static bool operator >=(StructDunderMethods left, StructDunderMethods right) => true;
}

public struct StructListMethods : IList<int>
{
    public int this[int index] { get => throw new NotImplementedException(); set => throw new NotImplementedException(); }
    public int Count => throw new NotImplementedException();
    public bool IsReadOnly => throw new NotImplementedException();
    public void Add(int item) { throw new NotImplementedException(); }
    public void Clear() { throw new NotImplementedException(); }
    public bool Contains(int item) { throw new NotImplementedException(); }
    public void CopyTo(int[] array, int arrayIndex) { throw new NotImplementedException(); }
    IEnumerator IEnumerable.GetEnumerator() { throw new NotImplementedException(); }
    public IEnumerator<int> GetEnumerator() { throw new NotImplementedException(); }
    public int IndexOf(int item) { throw new NotImplementedException(); }
    public void Insert(int index, int item) { throw new NotImplementedException(); }
    public bool Remove(int item) { throw new NotImplementedException(); }
    public void RemoveAt(int index) { throw new NotImplementedException(); }
}

public struct StructEvents { public event EventHandler A; public event EventHandler<EventArgs> B; }

public struct StructNested
{
    public class NestedClass;
    public struct NestedStruct;
    public record NestedRecord;
    public interface INested;
    public enum NestedEnum;
    public delegate void NestedDelegate();
}
