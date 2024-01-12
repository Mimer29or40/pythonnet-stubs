from __future__ import annotations

import clr


def main() -> None:
    assembly = clr.AddReference("StubgenTestLib")
    for type in assembly.GetTypes():
        print(type.Name)


if __name__ == "__main__":
    main()
