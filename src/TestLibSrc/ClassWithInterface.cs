namespace TestLib
{
    public class ClassWithInterface : IEquatable<ClassWithInterface>
    {
        public override bool Equals(object? obj) { throw new NotImplementedException(); }
        public bool Equals(ClassWithInterface? other) { throw new NotImplementedException(); }
        public override int GetHashCode() { throw new NotImplementedException(); }
    }
}
