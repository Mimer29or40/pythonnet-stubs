using System.Collections;

namespace TestLib
{
    public readonly struct StructWithListMethods : IList<int>
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
}
