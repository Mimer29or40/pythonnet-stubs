namespace TestLib
{
    public abstract class ClassThatsAbstract { }

    public class ClassWithSuper : ClassThatsAbstract { }

    public class ClassWithInterface : IEquatable<ClassWithInterface>
    {
        public override bool Equals(object? obj) { throw new NotImplementedException(); }
        public bool Equals(ClassWithInterface? other) { throw new NotImplementedException(); }
        public override int GetHashCode() { throw new NotImplementedException(); }
    }

    public class ClassWithGeneric<T> { }

    public class ClassWithMultiGeneric<U, V> { }

    public class ClassWithFields
    {
        public const int InstanceFieldA = 0;
        public const int InstanceFieldB = 1;
        public const int InstanceFieldC = 2;

        public static readonly int StaticFieldA = 0;
        public static readonly int StaticFieldB = 1;
        public static readonly int StaticFieldC = 2;
    }

    public class ClassWithConstructors
    {
        public ClassWithConstructors() { }
        public ClassWithConstructors(int param0) { }
        public ClassWithConstructors(int param0, int param1) { }
        public ClassWithConstructors(int param0, int param1, int param2) { }
    }

    public class ClassWithProperties
    {
        public int InstanceProperty0 { get; set; }
        public int InstanceProperty1 { get; set; }
        public int InstanceProperty2 { get; set; }
        public int InstanceReadOnlyProperty0 { get; }
        public int InstanceReadOnlyProperty1 { get; }
        public int InstanceReadOnlyProperty2 { get; }
        public static int StaticProperty0 { get; set; }
        public static int StaticProperty1 { get; set; }
        public static int StaticProperty2 { get; set; }
        public static int StaticReadOnlyProperty0 { get; }
        public static int StaticReadOnlyProperty1 { get; }
        public static int StaticReadOnlyProperty2 { get; }
    }

    public class ClassWithMethods
    {
        public int InstanceMethodWithDefaultParam(int param0 = 0) { return 0; }
        public int InstanceMethodWithNullableDefaultParam(int? param0 = 0) { param0 = 0; return 0; }
        public int InstanceMethodWithNullableOutParam(out int? param0) { param0 = 0; return 0; }
        public int InstanceMethodWithNullableParam(int? param0) { return 0; }
        public int InstanceMethodWithOutParam(out int param0) { param0 = 0; return 0; }
        public int InstanceMethodWithParams0() { return 0; }
        public int InstanceMethodWithParams1(int param0) { return 0; }
        public int InstanceMethodWithParams2(int param0, int param1) { return 0; }
        public static int StaticMethodWithDefaultParam(int param0 = 0) { return 0; }
        public static int StaticMethodWithNullableDefaultParam(int? param0 = 0) { param0 = 0; return 0; }
        public static int StaticMethodWithNullableOutParam(out int? param0) { param0 = 0; return 0; }
        public static int StaticMethodWithNullableParam(int? param0) { return 0; }
        public static int StaticMethodWithOutParam(out int param0) { param0 = 0; return 0; }
        public static int StaticMethodWithParams0() { return 0; }
        public static int StaticMethodWithParams1(int param0) { return 0; }
        public static int StaticMethodWithParams2(int param0, int param1) { return 0; }
    }
    public class ClassWithOperatorMethods
    {
        public override bool Equals(object? obj) { return base.Equals(obj); }
        public override int GetHashCode() { return base.GetHashCode(); }
        public static ClassWithOperatorMethods operator +(ClassWithOperatorMethods self) => new ClassWithOperatorMethods();
        public static ClassWithOperatorMethods operator -(ClassWithOperatorMethods self) => new ClassWithOperatorMethods();
        public static ClassWithOperatorMethods operator ++(ClassWithOperatorMethods self) => new ClassWithOperatorMethods();
        public static ClassWithOperatorMethods operator --(ClassWithOperatorMethods self) => new ClassWithOperatorMethods();
        public static ClassWithOperatorMethods operator +(ClassWithOperatorMethods self, ClassWithOperatorMethods other) => new ClassWithOperatorMethods();
        public static ClassWithOperatorMethods operator -(ClassWithOperatorMethods self, ClassWithOperatorMethods other) => new ClassWithOperatorMethods();
        public static ClassWithOperatorMethods operator *(ClassWithOperatorMethods self, ClassWithOperatorMethods other) => new ClassWithOperatorMethods();
        public static ClassWithOperatorMethods operator /(ClassWithOperatorMethods self, ClassWithOperatorMethods other) => new ClassWithOperatorMethods();
        public static ClassWithOperatorMethods operator %(ClassWithOperatorMethods self, ClassWithOperatorMethods other) => new ClassWithOperatorMethods();
        public static ClassWithOperatorMethods operator ~(ClassWithOperatorMethods self) => new ClassWithOperatorMethods();
        public static ClassWithOperatorMethods operator &(ClassWithOperatorMethods self, ClassWithOperatorMethods other) => new ClassWithOperatorMethods();
        public static ClassWithOperatorMethods operator |(ClassWithOperatorMethods self, ClassWithOperatorMethods other) => new ClassWithOperatorMethods();
        public static ClassWithOperatorMethods operator ^(ClassWithOperatorMethods self, ClassWithOperatorMethods other) => new ClassWithOperatorMethods();
        public static ClassWithOperatorMethods operator <<(ClassWithOperatorMethods self, ClassWithOperatorMethods other) => new ClassWithOperatorMethods();
        public static ClassWithOperatorMethods operator >>>(ClassWithOperatorMethods self, ClassWithOperatorMethods other) => new ClassWithOperatorMethods();
        public static bool operator !(ClassWithOperatorMethods self) => true;
        public static bool operator true(ClassWithOperatorMethods self) => true;
        public static bool operator false(ClassWithOperatorMethods self) => false;
        public static bool operator ==(ClassWithOperatorMethods self, ClassWithOperatorMethods other) => true;
        public static bool operator !=(ClassWithOperatorMethods self, ClassWithOperatorMethods other) => true;
        public static bool operator <(ClassWithOperatorMethods self, ClassWithOperatorMethods other) => true;
        public static bool operator <=(ClassWithOperatorMethods self, ClassWithOperatorMethods other) => true;
        public static bool operator >(ClassWithOperatorMethods self, ClassWithOperatorMethods other) => true;
        public static bool operator >=(ClassWithOperatorMethods self, ClassWithOperatorMethods other) => true;
    }

    public class ClassWithCollectionMethods : ICollection<int>
    {
        public int Count { get; }
        public bool IsReadOnly { get; }
        public void Add(int item) { }
        public void Clear() { }
        public bool Contains(int item) { return false; }
        public void CopyTo(int[] array, int arrayIndex) { }
        System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator() { throw new NotImplementedException(); }
        public IEnumerator<int> GetEnumerator() { throw new NotImplementedException(); }
        IEnumerator<int> IEnumerable<int>.GetEnumerator() { throw new NotImplementedException(); }
        public bool Remove(int item) { return false; }
    }

    public class ClassWithEvents
    {
        public event EventHandler? Event;
        public event EventHandler<EventArgs>? EventWitArgs;
    }

    public class ClassWithNested
    {
        public class NestedClass { }
        public struct NestedStruct { }
        public interface INestedInterface { }
        public enum NestedEnum { }
        public delegate void NestedDelegate();
    }
}
