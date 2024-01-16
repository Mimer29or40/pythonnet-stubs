namespace TestLib
{
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
        //public static ClassWithOperatorMethods operator <<(ClassWithOperatorMethods self, ClassWithOperatorMethods other) => new ClassWithOperatorMethods();
        //public static ClassWithOperatorMethods operator >>>(ClassWithOperatorMethods self, ClassWithOperatorMethods other) => new ClassWithOperatorMethods();
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
}
