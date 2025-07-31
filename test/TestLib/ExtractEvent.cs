namespace TestLib;

public class ExtractEvent
{
    public event EventHandler Basic;

    public event EventHandler<EventArgs> Arguments;
}