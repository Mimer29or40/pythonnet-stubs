namespace TestLib
{
    public struct StructWithOperatorMethods
    {
        public override readonly bool Equals(object? obj) { return base.Equals(obj); }
        public override readonly int GetHashCode() { return base.GetHashCode(); }
        public static StructWithOperatorMethods operator +(StructWithOperatorMethods self) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator -(StructWithOperatorMethods self) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator ++(StructWithOperatorMethods self) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator --(StructWithOperatorMethods self) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator +(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator -(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator *(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator /(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator %(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator ~(StructWithOperatorMethods self) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator &(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator |(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator ^(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        //public static StructWithOperatorMethods operator <<(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        //public static StructWithOperatorMethods operator >>>(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        public static bool operator !(StructWithOperatorMethods self) => true;
        public static bool operator true(StructWithOperatorMethods self) => true;
        public static bool operator false(StructWithOperatorMethods self) => false;
        public static bool operator ==(StructWithOperatorMethods self, StructWithOperatorMethods other) => true;
        public static bool operator !=(StructWithOperatorMethods self, StructWithOperatorMethods other) => true;
        public static bool operator <(StructWithOperatorMethods self, StructWithOperatorMethods other) => true;
        public static bool operator <=(StructWithOperatorMethods self, StructWithOperatorMethods other) => true;
        public static bool operator >(StructWithOperatorMethods self, StructWithOperatorMethods other) => true;
        public static bool operator >=(StructWithOperatorMethods self, StructWithOperatorMethods other) => true;
    }
}
