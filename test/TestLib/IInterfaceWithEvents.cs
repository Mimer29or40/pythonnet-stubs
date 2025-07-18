namespace TestLib
{
    public interface IInterfaceWithEvents
    {
        public event EventHandler? Event;
        public event EventHandler<EventArgs>? EventWithArgs;
    }
}
