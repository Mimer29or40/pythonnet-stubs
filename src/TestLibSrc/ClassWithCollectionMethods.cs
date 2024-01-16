namespace TestLib
{
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
}
