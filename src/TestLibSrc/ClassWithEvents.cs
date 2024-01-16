namespace TestLib
{
    public class ClassWithEvents
    {
        public event EventHandler? Event;
        public event EventHandler<EventArgs>? EventWithArgs;
    }
}
