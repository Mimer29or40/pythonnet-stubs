namespace TestLib
{
    public struct StructWithInterface : IEquatable<StructWithInterface>
    {
        public override bool Equals(object? obj) { throw new NotImplementedException(); }
        public bool Equals(StructWithInterface? other) { throw new NotImplementedException(); }
        public bool Equals(StructWithInterface other) { throw new NotImplementedException(); }
        public override int GetHashCode() { throw new NotImplementedException(); }
        public static bool operator ==(StructWithInterface left, StructWithInterface right) => true;
        public static bool operator !=(StructWithInterface left, StructWithInterface right) => false;
    }
}
