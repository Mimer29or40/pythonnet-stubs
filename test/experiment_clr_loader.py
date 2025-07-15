from __future__ import annotations

import sys

import clr

# import clr_loader

sys.path.append("C:/Projects/pythonnet-stubs/src/TestLibSrc/bin/Debug/net6.0")
print(sys.path)

# runtime = clr_loader.get_coreclr()
# print(runtime)


def main() -> None:
    asm0 = clr.AddReference("TestLib")
    print(asm0)
    # print(clr.GetClrType("TestLib.ClassWithSuper"))
    try:
        pass
    except Exception as e:
        print(e)

    # asm1 = runtime.get_assembly("C:/Projects/pythonnet-stubs/test/TestLib.dll")
    # print(asm1)
    # function = asm1.get_function("TestLib.ClassWithMethods.StaticMethodWithParams0")
    # print(function)


if __name__ == "__main__":
    main()
