namespace TestLib
{
    public interface IInterfaceWithOperatorMethods
    {
        public static IInterfaceWithOperatorMethods operator +(IInterfaceWithOperatorMethods self) { return self; }
        public static IInterfaceWithOperatorMethods operator -(IInterfaceWithOperatorMethods self) { return self; }
        public static IInterfaceWithOperatorMethods operator ++(IInterfaceWithOperatorMethods self) { return self; }
        public static IInterfaceWithOperatorMethods operator --(IInterfaceWithOperatorMethods self) { return self; }
        public static IInterfaceWithOperatorMethods operator +(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other) { return self; }
        public static IInterfaceWithOperatorMethods operator -(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other) { return self; }
        public static IInterfaceWithOperatorMethods operator *(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other) { return self; }
        public static IInterfaceWithOperatorMethods operator /(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other) { return self; }
        public static IInterfaceWithOperatorMethods operator %(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other) { return self; }
        public static IInterfaceWithOperatorMethods operator ~(IInterfaceWithOperatorMethods self) { return self; }
        public static IInterfaceWithOperatorMethods operator &(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other) { return self; }
        public static IInterfaceWithOperatorMethods operator |(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other) { return self; }
        public static IInterfaceWithOperatorMethods operator ^(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other) { return self; }
        //public static IInterfaceWithOperatorMethods operator <<(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other) { return self; }
        //public static IInterfaceWithOperatorMethods operator >>>(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other) { return self; }
        public static bool operator !(IInterfaceWithOperatorMethods self) { return true; }
        public static bool operator true(IInterfaceWithOperatorMethods self) { return true; }
        public static bool operator false(IInterfaceWithOperatorMethods self) { return true; }
        //public static bool operator ==(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other) { return true; }
        //public static bool operator !=(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other) { return true; }
        public static bool operator <(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other) { return true; }
        public static bool operator <=(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other) { return true; }
        public static bool operator >(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other) { return true; }
        public static bool operator >=(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other) { return true; }
    }
}
