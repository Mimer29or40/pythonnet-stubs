using System.Collections;

namespace TestLib;

public record RecordBasic;

public record RecordGeneric<TA, TB>;

public record RecordInterfaces : IComparable<object>
{
    public int CompareTo(object? other) { throw new NotImplementedException(); }
}

public record RecordFields { public RecordFields() { } public int A = 0; public int B = 0; }

public record RecordConstructors
{
    public RecordConstructors() { }
    public RecordConstructors(int param0, int param1) { }
}

public record RecordProperties { public int A { get; } public int B { get; set; } }

public record RecordMethods { public void A() { } public int B() { return 0; } }

public record RecordDunderMethods
{
    public static RecordDunderMethods operator +(RecordDunderMethods self) => self;
    public static RecordDunderMethods operator -(RecordDunderMethods self) => self;
    public static RecordDunderMethods operator ++(RecordDunderMethods self) => self;
    public static RecordDunderMethods operator --(RecordDunderMethods self) => self;
    public static RecordDunderMethods operator +(RecordDunderMethods left, RecordDunderMethods right) => left;
    public static RecordDunderMethods operator -(RecordDunderMethods left, RecordDunderMethods right) => left;
    public static RecordDunderMethods operator *(RecordDunderMethods left, RecordDunderMethods right) => left;
    public static RecordDunderMethods operator /(RecordDunderMethods left, RecordDunderMethods right) => left;
    public static RecordDunderMethods operator %(RecordDunderMethods left, RecordDunderMethods right) => left;
    public static RecordDunderMethods operator ~(RecordDunderMethods self) => self;
    public static RecordDunderMethods operator &(RecordDunderMethods left, RecordDunderMethods right) => left;
    public static RecordDunderMethods operator |(RecordDunderMethods left, RecordDunderMethods right) => left;
    public static RecordDunderMethods operator ^(RecordDunderMethods left, RecordDunderMethods right) => left;
    public static RecordDunderMethods operator <<(RecordDunderMethods left, RecordDunderMethods right) => left;
    public static RecordDunderMethods operator >>>(RecordDunderMethods left, RecordDunderMethods right) => left;
    public static bool operator !(RecordDunderMethods self) => true;
    public static bool operator true(RecordDunderMethods self) => true;
    public static bool operator false(RecordDunderMethods self) => false;
    public static bool operator <(RecordDunderMethods left, RecordDunderMethods right) => true;
    public static bool operator <=(RecordDunderMethods left, RecordDunderMethods right) => true;
    public static bool operator >(RecordDunderMethods left, RecordDunderMethods right) => true;
    public static bool operator >=(RecordDunderMethods left, RecordDunderMethods right) => true;
}

public record RecordListMethods : IList<int>
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

public record RecordEvents { public event EventHandler A; public event EventHandler<EventArgs> B; }

public record RecordNested
{
    public class NestedClass;
    public struct NestedStruct;
    public record NestedRecord;
    public interface INested;
    public enum NestedEnum;
    public delegate void NestedDelegate();
}