using System.Collections;

namespace TestLib;

public class ClassBasic;

public abstract class ClassAbstract;

public class ClassGeneric<TA, TB>;

public class ClassInterfaces : IComparable<object>, IEquatable<object>
{
    public int CompareTo(object? other) { throw new NotImplementedException(); }
}

public class ClassFields { public int A = 0; public int B = 0; }

public class ClassConstructors
{
    public ClassConstructors() { }
    public ClassConstructors(int param0, int param1) { }
}

public class ClassProperties { public int A { get; } = 0; public int B { get; set; } = 0; }

public class ClassMethods { public void A() { } public int B() { return 0; } }

public class ClassDunderMethods
{
    public static ClassDunderMethods operator +(ClassDunderMethods self) => self;
    public static ClassDunderMethods operator -(ClassDunderMethods self) => self;
    public static ClassDunderMethods operator ++(ClassDunderMethods self) => self;
    public static ClassDunderMethods operator --(ClassDunderMethods self) => self;
    public static ClassDunderMethods operator +(ClassDunderMethods left, ClassDunderMethods right) => left;
    public static ClassDunderMethods operator -(ClassDunderMethods left, ClassDunderMethods right) => left;
    public static ClassDunderMethods operator *(ClassDunderMethods left, ClassDunderMethods right) => left;
    public static ClassDunderMethods operator /(ClassDunderMethods left, ClassDunderMethods right) => left;
    public static ClassDunderMethods operator %(ClassDunderMethods left, ClassDunderMethods right) => left;
    public static ClassDunderMethods operator ~(ClassDunderMethods self) => self;
    public static ClassDunderMethods operator &(ClassDunderMethods left, ClassDunderMethods right) => left;
    public static ClassDunderMethods operator |(ClassDunderMethods left, ClassDunderMethods right) => left;
    public static ClassDunderMethods operator ^(ClassDunderMethods left, ClassDunderMethods right) => left;
    public static ClassDunderMethods operator <<(ClassDunderMethods left, ClassDunderMethods right) => left;
    public static ClassDunderMethods operator >>>(ClassDunderMethods left, ClassDunderMethods right) => left;
    public static bool operator !(ClassDunderMethods self) => true;
    public static bool operator true(ClassDunderMethods self) => true;
    public static bool operator false(ClassDunderMethods self) => false;
    public static bool operator ==(ClassDunderMethods left, ClassDunderMethods right) => true;
    public static bool operator !=(ClassDunderMethods left, ClassDunderMethods right) => true;
    public static bool operator <(ClassDunderMethods left, ClassDunderMethods right) => true;
    public static bool operator <=(ClassDunderMethods left, ClassDunderMethods right) => true;
    public static bool operator >(ClassDunderMethods left, ClassDunderMethods right) => true;
    public static bool operator >=(ClassDunderMethods left, ClassDunderMethods right) => true;
}

public class ClassListMethods : IList<int>
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

public class ClassEvents { public event EventHandler A; public event EventHandler<EventArgs> B; }

public class ClassNested
{
    public class NestedClass;
    public struct NestedStruct;
    public record NestedRecord;
    public interface INested;
    public enum NestedEnum;
    public delegate void NestedDelegate();
}
