import difflib
import pprint
import unittest
from typing import Mapping
from typing import Optional
from unittest.util import _common_shorten_repr  # noqa
from unittest.util import safe_repr

from stubgen.model import CClass
from stubgen.model import CConstructor
from stubgen.model import CDelegate
from stubgen.model import CEnum
from stubgen.model import CEvent
from stubgen.model import CField
from stubgen.model import CInterface
from stubgen.model import CMethod
from stubgen.model import CParameter
from stubgen.model import CProperty
from stubgen.model import CStruct
from stubgen.model import CType


class TestBase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.addTypeEqualityFunc(CClass, self.assertCClass)
        self.addTypeEqualityFunc(CStruct, self.assertCStruct)
        self.addTypeEqualityFunc(CInterface, self.assertCInterface)
        self.addTypeEqualityFunc(CEnum, self.assertCEnum)
        self.addTypeEqualityFunc(CDelegate, self.assertCDelegate)

        self.addTypeEqualityFunc(CType, self.assertCType)
        self.addTypeEqualityFunc(CParameter, self.assertCParameter)

        self.addTypeEqualityFunc(CField, self.assertCField)
        self.addTypeEqualityFunc(CConstructor, self.assertCConstructor)
        self.addTypeEqualityFunc(CProperty, self.assertCProperty)
        self.addTypeEqualityFunc(CMethod, self.assertCMethod)
        self.addTypeEqualityFunc(CEvent, self.assertCEvent)

    def assertMapping(self, map1: Mapping, map2: Mapping, msg: str = None) -> None:
        self.assertIsInstance(map1, Mapping, f"map1 is not a Mapping")
        self.assertIsInstance(map2, Mapping, f"map2 is not a Mapping")

        differing: Optional[str] = None
        len1 = 0
        try:
            len1 = len(map1)
        except (TypeError, NotImplementedError):
            differing = f"map1 has no length.    Non-mapping?"

        len2 = 0
        if differing is None:
            try:
                len2 = len(map2)
            except (TypeError, NotImplementedError):
                differing = f"map2 has no length.    Non-mapping?"

        if differing is None:
            if map1 == map2:
                return

            differing = "Mapping differ: %s != %s\n".format(*_common_shorten_repr(map1, map2))

            for i, (key1, key2) in enumerate(zip(map1, map2)):
                if key1 != key2:
                    differing += f"\nKeys at index {i} are different: {key1} != {key2}\n"
                    break

                try:
                    item1 = map1[key1]
                except (TypeError, IndexError, NotImplementedError):
                    differing += f"\nUnable to element at key {key1} of map1\n"
                    break

                try:
                    item2 = map2[key1]
                except (TypeError, IndexError, NotImplementedError):
                    differing += f"\nUnable to element at key {key2} of map2\n"
                    break

                if item1 != item2:
                    item_repr1, item_repr2 = _common_shorten_repr(item1, item2)
                    differing += f"\nFirst differing element {key1}:\n{item_repr1}\n{item_repr2}\n"
                    break

            if len1 > len2:
                differing += f"\nmap1 contains {len1 - len2} additional elements.\n"
                try:
                    differing += (
                        f"First extra element {len2}:\n{safe_repr(map1[list(map1)[len2]])}\n"
                    )
                except (TypeError, IndexError, NotImplementedError):
                    differing += f"Unable to index element {len2} of first Mapping\n"
            elif len1 < len2:
                differing += f"\nmap2 contains {len2 - len1} additional elements.\n"
                try:
                    differing += (
                        f"First extra element {len1}:\n{safe_repr(map2[list(map2)[len1]])}\n"
                    )
                except (TypeError, IndexError, NotImplementedError):
                    differing += f"Unable to index element {len1} of second Mapping\n"
        standard_msg: Optional[str] = differing
        diff_msg = "\n" + "\n".join(
            difflib.ndiff(pprint.pformat(map1).splitlines(), pprint.pformat(map2).splitlines())
        )

        standard_msg = self._truncateMessage(standard_msg, diff_msg)  # noqa
        msg = self._formatMessage(msg, standard_msg)
        self.fail(msg)

    def assertCClass(self, first: CClass, second: CClass, msg: str = None) -> None:
        self.assertIsInstance(first, CClass, "First argument is not a CClass")
        self.assertIsInstance(second, CClass, "Second argument is not a CClass")

        self.assertEqual(first.name, second.name, "Names are not equal")
        self.assertEqual(first.namespace, second.namespace, "Namespaces are not equal")
        self.assertEqual(first.generic_args, second.generic_args, "Generic args are not equal")
        self.assertEqual(first.super_class, second.super_class, "Super class are not equal")
        self.assertEqual(first.interfaces, second.interfaces, "Interfaces are not equal")

        self.assertMapping(first.fields, second.fields, "Fields are not equal")
        self.assertMapping(first.constructors, second.constructors, "Constructors are not equal")
        self.assertMapping(first.properties, second.properties, "Properties are not equal")
        self.assertMapping(first.methods, second.methods, "Methods are not equal")
        self.assertMapping(first.events, second.events, "Events are not equal")
        self.assertMapping(first.nested, second.nested, "Nested are not equal")

    def assertCStruct(self, first: CStruct, second: CStruct, msg: str = None) -> None:
        self.assertIsInstance(first, CStruct, "First argument is not a CStruct")
        self.assertIsInstance(second, CStruct, "Second argument is not a CStruct")

        self.assertEqual(first.name, second.name, "Names are not equal")
        self.assertEqual(first.namespace, second.namespace, "Namespaces are not equal")
        self.assertEqual(first.generic_args, second.generic_args, "Generic args are not equal")
        self.assertEqual(first.super_class, second.super_class, "Super class are not equal")
        self.assertEqual(first.interfaces, second.interfaces, "Interfaces are not equal")

        self.assertMapping(first.fields, second.fields, "Fields are not equal")
        self.assertMapping(first.constructors, second.constructors, "Constructors are not equal")
        self.assertMapping(first.properties, second.properties, "Properties are not equal")
        self.assertMapping(first.methods, second.methods, "Methods are not equal")
        self.assertMapping(first.events, second.events, "Events are not equal")
        self.assertMapping(first.nested, second.nested, "Nested are not equal")

    def assertCInterface(self, first: CInterface, second: CInterface, msg: str = None) -> None:
        self.assertIsInstance(first, CInterface, "First argument is not a CInterface")
        self.assertIsInstance(second, CInterface, "Second argument is not a CInterface")

        self.assertEqual(first.name, second.name, "Names are not equal")
        self.assertEqual(first.namespace, second.namespace, "Namespaces are not equal")
        self.assertEqual(first.generic_args, second.generic_args, "Generic args are not equal")
        self.assertEqual(first.interfaces, second.interfaces, "Interfaces are not equal")

        self.assertMapping(first.fields, second.fields, "Fields are not equal")
        self.assertMapping(first.properties, second.properties, "Properties are not equal")
        self.assertMapping(first.methods, second.methods, "Methods are not equal")
        self.assertMapping(first.events, second.events, "Events are not equal")
        self.assertMapping(first.nested, second.nested, "Nested are not equal")

    def assertCEnum(self, first: CEnum, second: CEnum, msg: str = None) -> None:
        self.assertIsInstance(first, CEnum, "First argument is not a CEnum")
        self.assertIsInstance(second, CEnum, "Second argument is not a CEnum")

        self.assertEqual(first.name, second.name, "Names are not equal")
        self.assertEqual(first.namespace, second.namespace, "Namespaces are not equal")
        self.assertEqual(first.fields, second.fields, "Fields are not equal")

    def assertCDelegate(self, first: CDelegate, second: CDelegate, msg: str = None) -> None:
        self.assertIsInstance(first, CDelegate, "First argument is not a CDelegate")
        self.assertIsInstance(second, CDelegate, "Second argument is not a CDelegate")

        self.assertEqual(first.name, second.name, "Names are not equal")
        self.assertEqual(first.namespace, second.namespace, "Namespaces are not equal")
        self.assertEqual(first.parameters, second.parameters, "Parameters are not equal")
        self.assertEqual(first.return_type, second.return_type, "Return type are not equal")

    def assertCType(self, first: CType, second: CType, msg: str = None) -> None:
        self.assertIsInstance(first, CType, "First argument is not a CType")
        self.assertIsInstance(second, CType, "Second argument is not a CType")

        self.assertEqual(first.name, second.name, "Names are not equal")
        self.assertEqual(first.namespace, second.namespace, "Namespaces are not equal")
        self.assertEqual(first.inner, second.inner, "Types are not equal")
        self.assertEqual(first.reference, second.reference, "References are not equal")
        self.assertEqual(first.generic, second.generic, "Generics are not equal")
        self.assertEqual(first.nullable, second.nullable, "Nullables are not equal")

    def assertCParameter(self, first: CParameter, second: CParameter, msg: str = None) -> None:
        self.assertIsInstance(first, CParameter, "First argument is not a CParameter")
        self.assertIsInstance(second, CParameter, "Second argument is not a CParameter")

        self.assertEqual(first.name, second.name, "Names are not equal")
        self.assertEqual(first.type, second.type, "Type are not equal")
        self.assertEqual(first.default, second.default, "Default are not equal")
        self.assertEqual(first.out, second.out, "Out are not equal")

    def assertCField(self, first: CField, second: CField, msg: str = None) -> None:
        self.assertIsInstance(first, CField, "First argument is not a CField")
        self.assertIsInstance(second, CField, "Second argument is not a CField")

        self.assertEqual(first.name, second.name, "Names are not equal")
        self.assertEqual(
            first.declaring_type, second.declaring_type, "Declaring types are not equal"
        )
        self.assertEqual(first.return_type, second.return_type, "Returns are not equal")
        self.assertEqual(first.static, second.static, "Static are not equal")

    def assertCConstructor(
        self, first: CConstructor, second: CConstructor, msg: str = None
    ) -> None:
        self.assertIsInstance(first, CConstructor, "First argument is not a CConstructor")
        self.assertIsInstance(second, CConstructor, "Second argument is not a CConstructor")

        self.assertEqual(first.name, second.name, "Names are not equal")
        self.assertEqual(
            first.declaring_type, second.declaring_type, "Declaring types are not equal"
        )
        self.assertEqual(first.parameters, second.parameters, "Parameters are not equal")

    def assertCProperty(self, first: CProperty, second: CProperty, msg: str = None) -> None:
        self.assertIsInstance(first, CProperty, "First argument is not a CProperty")
        self.assertIsInstance(second, CProperty, "Second argument is not a CProperty")

        self.assertEqual(first.name, second.name, "Names are not equal")
        self.assertEqual(
            first.declaring_type, second.declaring_type, "Declaring types are not equal"
        )
        self.assertEqual(first.type, second.type, "Type are not equal")
        self.assertEqual(first.setter, second.setter, "Setter are not equal")
        self.assertEqual(first.static, second.static, "Static are not equal")

    def assertCMethod(self, first: CMethod, second: CMethod, msg: str = None) -> None:
        self.assertIsInstance(first, CMethod, "First argument is not a CMethod")
        self.assertIsInstance(second, CMethod, "Second argument is not a CMethod")

        self.assertEqual(first.name, second.name, "Names are not equal")
        self.assertEqual(
            first.declaring_type, second.declaring_type, "Declaring types are not equal"
        )
        self.assertEqual(first.parameters, second.parameters, "Parameters are not equal")
        self.assertEqual(first.return_types, second.return_types, "Returns are not equal")
        self.assertEqual(first.static, second.static, "Static are not equal")

    def assertCEvent(self, first: CEvent, second: CEvent, msg: str = None) -> None:
        self.assertIsInstance(first, CEvent, "First argument is not a CEvent")
        self.assertIsInstance(second, CEvent, "Second argument is not a CEvent")

        self.assertEqual(first.name, second.name, "Names are not equal")
        self.assertEqual(
            first.declaring_type, second.declaring_type, "Declaring types are not equal"
        )
        self.assertEqual(first.type, second.type, "Types are not equal")
