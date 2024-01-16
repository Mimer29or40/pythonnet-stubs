namespace TestLib
{
    public struct StructWithEvents
    {
        public event EventHandler? Event;
        public event EventHandler<EventArgs>? EventWithArgs;
    }
}
