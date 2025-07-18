namespace TestLib
{
    public struct StructWithProperties
    {
        public int InstanceProperty0 { get; set; }
        public int InstanceProperty1 { get; set; }
        public int InstanceProperty2 { get; set; }
        public int InstanceReadOnlyProperty0 { get; }
        public int InstanceReadOnlyProperty1 { get; }
        public int InstanceReadOnlyProperty2 { get; }
        public static int StaticProperty0 { get; set; }
        public static int StaticProperty1 { get; set; }
        public static int StaticProperty2 { get; set; }
        public static int StaticReadOnlyProperty0 { get; }
        public static int StaticReadOnlyProperty1 { get; }
        public static int StaticReadOnlyProperty2 { get; }
    }
}
