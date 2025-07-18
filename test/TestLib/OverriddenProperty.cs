using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestLib
{
    public class OverriddenProperty : ClassWithProperties
    {
        new public int InstanceReadOnlyProperty0 { get; set; }
        new public int InstanceReadOnlyProperty1 { get; set; }
        new public int InstanceReadOnlyProperty2 { get; set; }
    }
}
