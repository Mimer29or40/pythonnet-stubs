from __future__ import annotations

from abc import ABC
from typing import List, Tuple, Union, overload

from System import Array, Attribute, Boolean, Byte, Decimal, Double, IComparable, IEquatable, IFormatProvider, IFormattable, Int16, Int32, Int64, Object, SByte, Single, String, UInt16, UInt32, UInt64, ValueType, Void
from System.Globalization import NumberStyles
from System.Runtime.InteropServices import _Attribute

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
DecimalType = Union[float, Decimal]
DoubleType = Union[float, Double]
FloatType = Union[float, Single]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
ObjectType = Object
SByteType = Union[int, SByte]
ShortType = Union[int, Int16]
StringType = Union[str, String]
UIntType = Union[int, UInt32]
ULongType = Union[int, UInt64]
UShortType = Union[int, UInt16]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class BigNumber(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HashCodeHelper(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class JitIntrinsicAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NumericsHelpers(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Abs(a: IntType) -> UIntType: ...
    
    @staticmethod
    @overload
    def CbitHighZero(u: UIntType) -> IntType: ...
    
    @staticmethod
    @overload
    def CbitHighZero(uu: ULongType) -> IntType: ...
    
    @staticmethod
    def CbitLowZero(u: UIntType) -> IntType: ...
    
    @staticmethod
    @overload
    def CombineHash(u1: UIntType, u2: UIntType) -> UIntType: ...
    
    @staticmethod
    @overload
    def CombineHash(n1: IntType, n2: IntType) -> IntType: ...
    
    @staticmethod
    def DangerousMakeTwosComplement(d: ArrayType[UIntType]) -> ArrayType[UIntType]: ...
    
    @staticmethod
    @overload
    def GCD(u1: UIntType, u2: UIntType) -> UIntType: ...
    
    @staticmethod
    @overload
    def GCD(uu1: ULongType, uu2: ULongType) -> ULongType: ...
    
    @staticmethod
    def GetDoubleFromParts(sign: IntType, exp: IntType, man: ULongType) -> DoubleType: ...
    
    @staticmethod
    def GetDoubleParts(dbl: DoubleType, sign: IntType, exp: IntType, man: ULongType, fFinite: BooleanType) -> Tuple[VoidType, IntType, IntType, ULongType, BooleanType]: ...
    
    @staticmethod
    def GetHi(uu: ULongType) -> UIntType: ...
    
    @staticmethod
    def GetLo(uu: ULongType) -> UIntType: ...
    
    @staticmethod
    def MakeUlong(uHi: UIntType, uLo: UIntType) -> ULongType: ...
    
    @staticmethod
    def Swap(a: T, b: T) -> Tuple[VoidType, T, T]: ...
    
    @staticmethod
    def resize(v: ArrayType[UIntType], len: IntType) -> ArrayType[UIntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Vector(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def IsHardwareAccelerated() -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_IsHardwareAccelerated() -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class BigInteger(ValueType, IFormattable, IComparable, IComparable[BigInteger], IEquatable[BigInteger]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, value: IntType): ...
    
    @overload
    def __init__(self, value: UIntType): ...
    
    @overload
    def __init__(self, value: LongType): ...
    
    @overload
    def __init__(self, value: ULongType): ...
    
    @overload
    def __init__(self, value: FloatType): ...
    
    @overload
    def __init__(self, value: DoubleType): ...
    
    @overload
    def __init__(self, value: DecimalType): ...
    
    @overload
    def __init__(self, value: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsEven(self) -> BooleanType: ...
    
    @property
    def IsOne(self) -> BooleanType: ...
    
    @property
    def IsPowerOfTwo(self) -> BooleanType: ...
    
    @property
    def IsZero(self) -> BooleanType: ...
    
    @staticmethod
    @property
    def MinusOne() -> BigInteger: ...
    
    @staticmethod
    @property
    def One() -> BigInteger: ...
    
    @property
    def Sign(self) -> IntType: ...
    
    @staticmethod
    @property
    def Zero() -> BigInteger: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Abs(value: BigInteger) -> BigInteger: ...
    
    @staticmethod
    def Add(left: BigInteger, right: BigInteger) -> BigInteger: ...
    
    @staticmethod
    def Compare(left: BigInteger, right: BigInteger) -> IntType: ...
    
    @overload
    def CompareTo(self, other: LongType) -> IntType: ...
    
    @overload
    def CompareTo(self, other: ULongType) -> IntType: ...
    
    @overload
    def CompareTo(self, other: BigInteger) -> IntType: ...
    
    @overload
    def CompareTo(self, obj: ObjectType) -> IntType: ...
    
    @staticmethod
    def DivRem(dividend: BigInteger, divisor: BigInteger, remainder: BigInteger) -> Tuple[BigInteger, BigInteger]: ...
    
    @staticmethod
    def Divide(dividend: BigInteger, divisor: BigInteger) -> BigInteger: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: LongType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: ULongType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: BigInteger) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def GreatestCommonDivisor(left: BigInteger, right: BigInteger) -> BigInteger: ...
    
    @staticmethod
    @overload
    def Log(value: BigInteger) -> DoubleType: ...
    
    @staticmethod
    @overload
    def Log(value: BigInteger, baseValue: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def Log10(value: BigInteger) -> DoubleType: ...
    
    @staticmethod
    def Max(left: BigInteger, right: BigInteger) -> BigInteger: ...
    
    @staticmethod
    def Min(left: BigInteger, right: BigInteger) -> BigInteger: ...
    
    @staticmethod
    def ModPow(value: BigInteger, exponent: BigInteger, modulus: BigInteger) -> BigInteger: ...
    
    @staticmethod
    def Multiply(left: BigInteger, right: BigInteger) -> BigInteger: ...
    
    @staticmethod
    def Negate(value: BigInteger) -> BigInteger: ...
    
    @staticmethod
    @overload
    def Parse(value: StringType) -> BigInteger: ...
    
    @staticmethod
    @overload
    def Parse(value: StringType, style: NumberStyles) -> BigInteger: ...
    
    @staticmethod
    @overload
    def Parse(value: StringType, provider: IFormatProvider) -> BigInteger: ...
    
    @staticmethod
    @overload
    def Parse(value: StringType, style: NumberStyles, provider: IFormatProvider) -> BigInteger: ...
    
    @staticmethod
    def Pow(value: BigInteger, exponent: IntType) -> BigInteger: ...
    
    @staticmethod
    def Remainder(dividend: BigInteger, divisor: BigInteger) -> BigInteger: ...
    
    @staticmethod
    def Subtract(left: BigInteger, right: BigInteger) -> BigInteger: ...
    
    def ToByteArray(self) -> ArrayType[ByteType]: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def TryParse(value: StringType, result: BigInteger) -> Tuple[BooleanType, BigInteger]: ...
    
    @staticmethod
    @overload
    def TryParse(value: StringType, style: NumberStyles, provider: IFormatProvider, result: BigInteger) -> Tuple[BooleanType, BigInteger]: ...
    
    def get_IsEven(self) -> BooleanType: ...
    
    def get_IsOne(self) -> BooleanType: ...
    
    def get_IsPowerOfTwo(self) -> BooleanType: ...
    
    def get_IsZero(self) -> BooleanType: ...
    
    @staticmethod
    def get_MinusOne() -> BigInteger: ...
    
    @staticmethod
    def get_One() -> BigInteger: ...
    
    def get_Sign(self) -> IntType: ...
    
    @staticmethod
    def get_Zero() -> BigInteger: ...
    
    @staticmethod
    def op_Addition(left: BigInteger, right: BigInteger) -> BigInteger: ...
    
    @staticmethod
    def op_BitwiseAnd(left: BigInteger, right: BigInteger) -> BigInteger: ...
    
    @staticmethod
    def op_BitwiseOr(left: BigInteger, right: BigInteger) -> BigInteger: ...
    
    @staticmethod
    def op_Decrement(value: BigInteger) -> BigInteger: ...
    
    @staticmethod
    def op_Division(dividend: BigInteger, divisor: BigInteger) -> BigInteger: ...
    
    @staticmethod
    @overload
    def op_Equality(left: BigInteger, right: BigInteger) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Equality(left: BigInteger, right: LongType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Equality(left: LongType, right: BigInteger) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Equality(left: BigInteger, right: ULongType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Equality(left: ULongType, right: BigInteger) -> BooleanType: ...
    
    @staticmethod
    def op_ExclusiveOr(left: BigInteger, right: BigInteger) -> BigInteger: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: FloatType) -> BigInteger: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: DoubleType) -> BigInteger: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: DecimalType) -> BigInteger: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: BigInteger) -> ByteType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: BigInteger) -> SByteType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: BigInteger) -> ShortType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: BigInteger) -> UShortType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: BigInteger) -> IntType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: BigInteger) -> UIntType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: BigInteger) -> LongType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: BigInteger) -> ULongType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: BigInteger) -> FloatType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: BigInteger) -> DoubleType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: BigInteger) -> DecimalType: ...
    
    @staticmethod
    @overload
    def op_GreaterThan(left: BigInteger, right: BigInteger) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_GreaterThan(left: BigInteger, right: LongType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_GreaterThan(left: LongType, right: BigInteger) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_GreaterThan(left: BigInteger, right: ULongType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_GreaterThan(left: ULongType, right: BigInteger) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_GreaterThanOrEqual(left: BigInteger, right: BigInteger) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_GreaterThanOrEqual(left: BigInteger, right: LongType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_GreaterThanOrEqual(left: LongType, right: BigInteger) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_GreaterThanOrEqual(left: BigInteger, right: ULongType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_GreaterThanOrEqual(left: ULongType, right: BigInteger) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: ByteType) -> BigInteger: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: SByteType) -> BigInteger: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: ShortType) -> BigInteger: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: UShortType) -> BigInteger: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: IntType) -> BigInteger: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: LongType) -> BigInteger: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: ULongType) -> BigInteger: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: UIntType) -> BigInteger: ...
    
    @staticmethod
    def op_Increment(value: BigInteger) -> BigInteger: ...
    
    @staticmethod
    @overload
    def op_Inequality(left: BigInteger, right: BigInteger) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Inequality(left: BigInteger, right: LongType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Inequality(left: LongType, right: BigInteger) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Inequality(left: BigInteger, right: ULongType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Inequality(left: ULongType, right: BigInteger) -> BooleanType: ...
    
    @staticmethod
    def op_LeftShift(value: BigInteger, shift: IntType) -> BigInteger: ...
    
    @staticmethod
    @overload
    def op_LessThan(left: BigInteger, right: BigInteger) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_LessThan(left: BigInteger, right: LongType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_LessThan(left: LongType, right: BigInteger) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_LessThan(left: BigInteger, right: ULongType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_LessThan(left: ULongType, right: BigInteger) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_LessThanOrEqual(left: BigInteger, right: BigInteger) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_LessThanOrEqual(left: BigInteger, right: LongType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_LessThanOrEqual(left: LongType, right: BigInteger) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_LessThanOrEqual(left: BigInteger, right: ULongType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_LessThanOrEqual(left: ULongType, right: BigInteger) -> BooleanType: ...
    
    @staticmethod
    def op_Modulus(dividend: BigInteger, divisor: BigInteger) -> BigInteger: ...
    
    @staticmethod
    def op_Multiply(left: BigInteger, right: BigInteger) -> BigInteger: ...
    
    @staticmethod
    def op_OnesComplement(value: BigInteger) -> BigInteger: ...
    
    @staticmethod
    def op_RightShift(value: BigInteger, shift: IntType) -> BigInteger: ...
    
    @staticmethod
    def op_Subtraction(left: BigInteger, right: BigInteger) -> BigInteger: ...
    
    @staticmethod
    def op_UnaryNegation(value: BigInteger) -> BigInteger: ...
    
    @staticmethod
    def op_UnaryPlus(value: BigInteger) -> BigInteger: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BigIntegerBuilder(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, reg: BigIntegerBuilder): ...
    
    @overload
    def __init__(self, cuAlloc: IntType): ...
    
    @overload
    def __init__(self, bn: BigInteger): ...
    
    @overload
    def __init__(self, bn: BigInteger, sign: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def High(self) -> UIntType: ...
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, reg: BigIntegerBuilder) -> Tuple[VoidType, BigIntegerBuilder]: ...
    
    @overload
    def Add(self, u: UIntType) -> VoidType: ...
    
    def CbitLowZero(self) -> IntType: ...
    
    def Div(self, regDen: BigIntegerBuilder) -> Tuple[VoidType, BigIntegerBuilder]: ...
    
    def DivMod(self, uDen: UIntType) -> UIntType: ...
    
    @overload
    def EnsureWritable(self, cu: IntType, cuExtra: IntType) -> VoidType: ...
    
    @overload
    def EnsureWritable(self, cuExtra: IntType) -> VoidType: ...
    
    @overload
    def EnsureWritable(self) -> VoidType: ...
    
    @staticmethod
    def GCD(reg1: BigIntegerBuilder, reg2: BigIntegerBuilder) -> Tuple[VoidType, BigIntegerBuilder, BigIntegerBuilder]: ...
    
    def GetApproxParts(self, exp: IntType, man: ULongType) -> Tuple[VoidType, IntType, ULongType]: ...
    
    def GetInteger(self, sign: IntType) -> BigInteger: ...
    
    @overload
    def Load(self, reg: BigIntegerBuilder) -> Tuple[VoidType, BigIntegerBuilder]: ...
    
    @overload
    def Load(self, reg: BigIntegerBuilder, cuExtra: IntType) -> Tuple[VoidType, BigIntegerBuilder]: ...
    
    def MakeOdd(self) -> IntType: ...
    
    @staticmethod
    @overload
    def Mod(regNum: BigIntegerBuilder, uDen: UIntType) -> Tuple[UIntType, BigIntegerBuilder]: ...
    
    @overload
    def Mod(self, regDen: BigIntegerBuilder) -> Tuple[VoidType, BigIntegerBuilder]: ...
    
    def ModDiv(self, regDen: BigIntegerBuilder, regQuo: BigIntegerBuilder) -> Tuple[VoidType, BigIntegerBuilder, BigIntegerBuilder]: ...
    
    @overload
    def Mul(self, regMul: BigIntegerBuilder) -> Tuple[VoidType, BigIntegerBuilder]: ...
    
    @overload
    def Mul(self, reg1: BigIntegerBuilder, reg2: BigIntegerBuilder) -> Tuple[VoidType, BigIntegerBuilder, BigIntegerBuilder]: ...
    
    @overload
    def Mul(self, u: UIntType) -> VoidType: ...
    
    @overload
    def Set(self, u: UIntType) -> VoidType: ...
    
    @overload
    def Set(self, uu: ULongType) -> VoidType: ...
    
    @overload
    def ShiftLeft(self, cbit: IntType) -> VoidType: ...
    
    @overload
    def ShiftLeft(self, cuShift: IntType, cbitShift: IntType) -> VoidType: ...
    
    @overload
    def ShiftRight(self, cbit: IntType) -> VoidType: ...
    
    @overload
    def ShiftRight(self, cuShift: IntType, cbitShift: IntType) -> VoidType: ...
    
    @overload
    def Sub(self, sign: IntType, u: UIntType) -> Tuple[VoidType, IntType]: ...
    
    @overload
    def Sub(self, sign: IntType, reg: BigIntegerBuilder) -> Tuple[VoidType, IntType, BigIntegerBuilder]: ...
    
    def get_High(self) -> UIntType: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Complex(ValueType, IEquatable[Complex], IFormattable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def ImaginaryOne() -> Complex: ...
    
    @staticmethod
    @property
    def One() -> Complex: ...
    
    @staticmethod
    @property
    def Zero() -> Complex: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, real: DoubleType, imaginary: DoubleType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Imaginary(self) -> DoubleType: ...
    
    @property
    def Magnitude(self) -> DoubleType: ...
    
    @property
    def Phase(self) -> DoubleType: ...
    
    @property
    def Real(self) -> DoubleType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Abs(value: Complex) -> DoubleType: ...
    
    @staticmethod
    def Acos(value: Complex) -> Complex: ...
    
    @staticmethod
    def Add(left: Complex, right: Complex) -> Complex: ...
    
    @staticmethod
    def Asin(value: Complex) -> Complex: ...
    
    @staticmethod
    def Atan(value: Complex) -> Complex: ...
    
    @staticmethod
    def Conjugate(value: Complex) -> Complex: ...
    
    @staticmethod
    def Cos(value: Complex) -> Complex: ...
    
    @staticmethod
    def Cosh(value: Complex) -> Complex: ...
    
    @staticmethod
    def Divide(dividend: Complex, divisor: Complex) -> Complex: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, value: Complex) -> BooleanType: ...
    
    @staticmethod
    def Exp(value: Complex) -> Complex: ...
    
    @staticmethod
    def FromPolarCoordinates(magnitude: DoubleType, phase: DoubleType) -> Complex: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    @overload
    def Log(value: Complex) -> Complex: ...
    
    @staticmethod
    @overload
    def Log(value: Complex, baseValue: DoubleType) -> Complex: ...
    
    @staticmethod
    def Log10(value: Complex) -> Complex: ...
    
    @staticmethod
    def Multiply(left: Complex, right: Complex) -> Complex: ...
    
    @staticmethod
    def Negate(value: Complex) -> Complex: ...
    
    @staticmethod
    @overload
    def Pow(value: Complex, power: Complex) -> Complex: ...
    
    @staticmethod
    @overload
    def Pow(value: Complex, power: DoubleType) -> Complex: ...
    
    @staticmethod
    def Reciprocal(value: Complex) -> Complex: ...
    
    @staticmethod
    def Sin(value: Complex) -> Complex: ...
    
    @staticmethod
    def Sinh(value: Complex) -> Complex: ...
    
    @staticmethod
    def Sqrt(value: Complex) -> Complex: ...
    
    @staticmethod
    def Subtract(left: Complex, right: Complex) -> Complex: ...
    
    @staticmethod
    def Tan(value: Complex) -> Complex: ...
    
    @staticmethod
    def Tanh(value: Complex) -> Complex: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, provider: IFormatProvider) -> StringType: ...
    
    def get_Imaginary(self) -> DoubleType: ...
    
    def get_Magnitude(self) -> DoubleType: ...
    
    def get_Phase(self) -> DoubleType: ...
    
    def get_Real(self) -> DoubleType: ...
    
    @staticmethod
    def op_Addition(left: Complex, right: Complex) -> Complex: ...
    
    @staticmethod
    def op_Division(left: Complex, right: Complex) -> Complex: ...
    
    @staticmethod
    def op_Equality(left: Complex, right: Complex) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: BigInteger) -> Complex: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: DecimalType) -> Complex: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: ShortType) -> Complex: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: IntType) -> Complex: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: LongType) -> Complex: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: UShortType) -> Complex: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: UIntType) -> Complex: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: ULongType) -> Complex: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: SByteType) -> Complex: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: ByteType) -> Complex: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: FloatType) -> Complex: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: DoubleType) -> Complex: ...
    
    @staticmethod
    def op_Inequality(left: Complex, right: Complex) -> BooleanType: ...
    
    @staticmethod
    def op_Multiply(left: Complex, right: Complex) -> Complex: ...
    
    @staticmethod
    def op_Subtraction(left: Complex, right: Complex) -> Complex: ...
    
    @staticmethod
    def op_UnaryNegation(value: Complex) -> Complex: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DoubleUlong(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def dbl(self) -> DoubleType: ...
    
    @dbl.setter
    def dbl(self, value: DoubleType) -> None: ...
    
    @property
    def uu(self) -> ULongType: ...
    
    @uu.setter
    def uu(self, value: ULongType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Matrix3x2(ValueType, IEquatable[Matrix3x2]):
    # ---------- Fields ---------- #
    
    @property
    def M11(self) -> FloatType: ...
    
    @M11.setter
    def M11(self, value: FloatType) -> None: ...
    
    @property
    def M12(self) -> FloatType: ...
    
    @M12.setter
    def M12(self, value: FloatType) -> None: ...
    
    @property
    def M21(self) -> FloatType: ...
    
    @M21.setter
    def M21(self, value: FloatType) -> None: ...
    
    @property
    def M22(self) -> FloatType: ...
    
    @M22.setter
    def M22(self, value: FloatType) -> None: ...
    
    @property
    def M31(self) -> FloatType: ...
    
    @M31.setter
    def M31(self, value: FloatType) -> None: ...
    
    @property
    def M32(self) -> FloatType: ...
    
    @M32.setter
    def M32(self, value: FloatType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, m11: FloatType, m12: FloatType, m21: FloatType, m22: FloatType, m31: FloatType, m32: FloatType): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Identity() -> Matrix3x2: ...
    
    @property
    def IsIdentity(self) -> BooleanType: ...
    
    @property
    def Translation(self) -> Vector2: ...
    
    @Translation.setter
    def Translation(self, value: Vector2) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Add(value1: Matrix3x2, value2: Matrix3x2) -> Matrix3x2: ...
    
    @staticmethod
    @overload
    def CreateRotation(radians: FloatType) -> Matrix3x2: ...
    
    @staticmethod
    @overload
    def CreateRotation(radians: FloatType, centerPoint: Vector2) -> Matrix3x2: ...
    
    @staticmethod
    @overload
    def CreateScale(xScale: FloatType, yScale: FloatType) -> Matrix3x2: ...
    
    @staticmethod
    @overload
    def CreateScale(xScale: FloatType, yScale: FloatType, centerPoint: Vector2) -> Matrix3x2: ...
    
    @staticmethod
    @overload
    def CreateScale(scales: Vector2) -> Matrix3x2: ...
    
    @staticmethod
    @overload
    def CreateScale(scales: Vector2, centerPoint: Vector2) -> Matrix3x2: ...
    
    @staticmethod
    @overload
    def CreateScale(scale: FloatType) -> Matrix3x2: ...
    
    @staticmethod
    @overload
    def CreateScale(scale: FloatType, centerPoint: Vector2) -> Matrix3x2: ...
    
    @staticmethod
    @overload
    def CreateSkew(radiansX: FloatType, radiansY: FloatType) -> Matrix3x2: ...
    
    @staticmethod
    @overload
    def CreateSkew(radiansX: FloatType, radiansY: FloatType, centerPoint: Vector2) -> Matrix3x2: ...
    
    @staticmethod
    @overload
    def CreateTranslation(position: Vector2) -> Matrix3x2: ...
    
    @staticmethod
    @overload
    def CreateTranslation(xPosition: FloatType, yPosition: FloatType) -> Matrix3x2: ...
    
    @overload
    def Equals(self, other: Matrix3x2) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetDeterminant(self) -> FloatType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def Invert(matrix: Matrix3x2, result: Matrix3x2) -> Tuple[BooleanType, Matrix3x2]: ...
    
    @staticmethod
    def Lerp(matrix1: Matrix3x2, matrix2: Matrix3x2, amount: FloatType) -> Matrix3x2: ...
    
    @staticmethod
    @overload
    def Multiply(value1: Matrix3x2, value2: Matrix3x2) -> Matrix3x2: ...
    
    @staticmethod
    @overload
    def Multiply(value1: Matrix3x2, value2: FloatType) -> Matrix3x2: ...
    
    @staticmethod
    def Negate(value: Matrix3x2) -> Matrix3x2: ...
    
    @staticmethod
    def Subtract(value1: Matrix3x2, value2: Matrix3x2) -> Matrix3x2: ...
    
    def ToString(self) -> StringType: ...
    
    @staticmethod
    def get_Identity() -> Matrix3x2: ...
    
    def get_IsIdentity(self) -> BooleanType: ...
    
    def get_Translation(self) -> Vector2: ...
    
    @staticmethod
    def op_Addition(value1: Matrix3x2, value2: Matrix3x2) -> Matrix3x2: ...
    
    @staticmethod
    def op_Equality(value1: Matrix3x2, value2: Matrix3x2) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(value1: Matrix3x2, value2: Matrix3x2) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Multiply(value1: Matrix3x2, value2: Matrix3x2) -> Matrix3x2: ...
    
    @staticmethod
    @overload
    def op_Multiply(value1: Matrix3x2, value2: FloatType) -> Matrix3x2: ...
    
    @staticmethod
    def op_Subtraction(value1: Matrix3x2, value2: Matrix3x2) -> Matrix3x2: ...
    
    @staticmethod
    def op_UnaryNegation(value: Matrix3x2) -> Matrix3x2: ...
    
    def set_Translation(self, value: Vector2) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Matrix4x4(ValueType, IEquatable[Matrix4x4]):
    # ---------- Fields ---------- #
    
    @property
    def M11(self) -> FloatType: ...
    
    @M11.setter
    def M11(self, value: FloatType) -> None: ...
    
    @property
    def M12(self) -> FloatType: ...
    
    @M12.setter
    def M12(self, value: FloatType) -> None: ...
    
    @property
    def M13(self) -> FloatType: ...
    
    @M13.setter
    def M13(self, value: FloatType) -> None: ...
    
    @property
    def M14(self) -> FloatType: ...
    
    @M14.setter
    def M14(self, value: FloatType) -> None: ...
    
    @property
    def M21(self) -> FloatType: ...
    
    @M21.setter
    def M21(self, value: FloatType) -> None: ...
    
    @property
    def M22(self) -> FloatType: ...
    
    @M22.setter
    def M22(self, value: FloatType) -> None: ...
    
    @property
    def M23(self) -> FloatType: ...
    
    @M23.setter
    def M23(self, value: FloatType) -> None: ...
    
    @property
    def M24(self) -> FloatType: ...
    
    @M24.setter
    def M24(self, value: FloatType) -> None: ...
    
    @property
    def M31(self) -> FloatType: ...
    
    @M31.setter
    def M31(self, value: FloatType) -> None: ...
    
    @property
    def M32(self) -> FloatType: ...
    
    @M32.setter
    def M32(self, value: FloatType) -> None: ...
    
    @property
    def M33(self) -> FloatType: ...
    
    @M33.setter
    def M33(self, value: FloatType) -> None: ...
    
    @property
    def M34(self) -> FloatType: ...
    
    @M34.setter
    def M34(self, value: FloatType) -> None: ...
    
    @property
    def M41(self) -> FloatType: ...
    
    @M41.setter
    def M41(self, value: FloatType) -> None: ...
    
    @property
    def M42(self) -> FloatType: ...
    
    @M42.setter
    def M42(self, value: FloatType) -> None: ...
    
    @property
    def M43(self) -> FloatType: ...
    
    @M43.setter
    def M43(self, value: FloatType) -> None: ...
    
    @property
    def M44(self) -> FloatType: ...
    
    @M44.setter
    def M44(self, value: FloatType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, m11: FloatType, m12: FloatType, m13: FloatType, m14: FloatType, m21: FloatType, m22: FloatType, m23: FloatType, m24: FloatType, m31: FloatType, m32: FloatType, m33: FloatType, m34: FloatType, m41: FloatType, m42: FloatType, m43: FloatType, m44: FloatType): ...
    
    @overload
    def __init__(self, value: Matrix3x2): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Identity() -> Matrix4x4: ...
    
    @property
    def IsIdentity(self) -> BooleanType: ...
    
    @property
    def Translation(self) -> Vector3: ...
    
    @Translation.setter
    def Translation(self, value: Vector3) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Add(value1: Matrix4x4, value2: Matrix4x4) -> Matrix4x4: ...
    
    @staticmethod
    def CreateBillboard(objectPosition: Vector3, cameraPosition: Vector3, cameraUpVector: Vector3, cameraForwardVector: Vector3) -> Matrix4x4: ...
    
    @staticmethod
    def CreateConstrainedBillboard(objectPosition: Vector3, cameraPosition: Vector3, rotateAxis: Vector3, cameraForwardVector: Vector3, objectForwardVector: Vector3) -> Matrix4x4: ...
    
    @staticmethod
    def CreateFromAxisAngle(axis: Vector3, angle: FloatType) -> Matrix4x4: ...
    
    @staticmethod
    def CreateFromQuaternion(quaternion: Quaternion) -> Matrix4x4: ...
    
    @staticmethod
    def CreateFromYawPitchRoll(yaw: FloatType, pitch: FloatType, roll: FloatType) -> Matrix4x4: ...
    
    @staticmethod
    def CreateLookAt(cameraPosition: Vector3, cameraTarget: Vector3, cameraUpVector: Vector3) -> Matrix4x4: ...
    
    @staticmethod
    def CreateOrthographic(width: FloatType, height: FloatType, zNearPlane: FloatType, zFarPlane: FloatType) -> Matrix4x4: ...
    
    @staticmethod
    def CreateOrthographicOffCenter(left: FloatType, right: FloatType, bottom: FloatType, top: FloatType, zNearPlane: FloatType, zFarPlane: FloatType) -> Matrix4x4: ...
    
    @staticmethod
    def CreatePerspective(width: FloatType, height: FloatType, nearPlaneDistance: FloatType, farPlaneDistance: FloatType) -> Matrix4x4: ...
    
    @staticmethod
    def CreatePerspectiveFieldOfView(fieldOfView: FloatType, aspectRatio: FloatType, nearPlaneDistance: FloatType, farPlaneDistance: FloatType) -> Matrix4x4: ...
    
    @staticmethod
    def CreatePerspectiveOffCenter(left: FloatType, right: FloatType, bottom: FloatType, top: FloatType, nearPlaneDistance: FloatType, farPlaneDistance: FloatType) -> Matrix4x4: ...
    
    @staticmethod
    def CreateReflection(value: Plane) -> Matrix4x4: ...
    
    @staticmethod
    @overload
    def CreateRotationX(radians: FloatType) -> Matrix4x4: ...
    
    @staticmethod
    @overload
    def CreateRotationX(radians: FloatType, centerPoint: Vector3) -> Matrix4x4: ...
    
    @staticmethod
    @overload
    def CreateRotationY(radians: FloatType) -> Matrix4x4: ...
    
    @staticmethod
    @overload
    def CreateRotationY(radians: FloatType, centerPoint: Vector3) -> Matrix4x4: ...
    
    @staticmethod
    @overload
    def CreateRotationZ(radians: FloatType) -> Matrix4x4: ...
    
    @staticmethod
    @overload
    def CreateRotationZ(radians: FloatType, centerPoint: Vector3) -> Matrix4x4: ...
    
    @staticmethod
    @overload
    def CreateScale(xScale: FloatType, yScale: FloatType, zScale: FloatType) -> Matrix4x4: ...
    
    @staticmethod
    @overload
    def CreateScale(xScale: FloatType, yScale: FloatType, zScale: FloatType, centerPoint: Vector3) -> Matrix4x4: ...
    
    @staticmethod
    @overload
    def CreateScale(scales: Vector3) -> Matrix4x4: ...
    
    @staticmethod
    @overload
    def CreateScale(scales: Vector3, centerPoint: Vector3) -> Matrix4x4: ...
    
    @staticmethod
    @overload
    def CreateScale(scale: FloatType) -> Matrix4x4: ...
    
    @staticmethod
    @overload
    def CreateScale(scale: FloatType, centerPoint: Vector3) -> Matrix4x4: ...
    
    @staticmethod
    def CreateShadow(lightDirection: Vector3, plane: Plane) -> Matrix4x4: ...
    
    @staticmethod
    @overload
    def CreateTranslation(position: Vector3) -> Matrix4x4: ...
    
    @staticmethod
    @overload
    def CreateTranslation(xPosition: FloatType, yPosition: FloatType, zPosition: FloatType) -> Matrix4x4: ...
    
    @staticmethod
    def CreateWorld(position: Vector3, forward: Vector3, up: Vector3) -> Matrix4x4: ...
    
    @staticmethod
    def Decompose(matrix: Matrix4x4, scale: Vector3, rotation: Quaternion, translation: Vector3) -> Tuple[BooleanType, Vector3, Quaternion, Vector3]: ...
    
    @overload
    def Equals(self, other: Matrix4x4) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetDeterminant(self) -> FloatType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def Invert(matrix: Matrix4x4, result: Matrix4x4) -> Tuple[BooleanType, Matrix4x4]: ...
    
    @staticmethod
    def Lerp(matrix1: Matrix4x4, matrix2: Matrix4x4, amount: FloatType) -> Matrix4x4: ...
    
    @staticmethod
    @overload
    def Multiply(value1: Matrix4x4, value2: Matrix4x4) -> Matrix4x4: ...
    
    @staticmethod
    @overload
    def Multiply(value1: Matrix4x4, value2: FloatType) -> Matrix4x4: ...
    
    @staticmethod
    def Negate(value: Matrix4x4) -> Matrix4x4: ...
    
    @staticmethod
    def Subtract(value1: Matrix4x4, value2: Matrix4x4) -> Matrix4x4: ...
    
    def ToString(self) -> StringType: ...
    
    @staticmethod
    def Transform(value: Matrix4x4, rotation: Quaternion) -> Matrix4x4: ...
    
    @staticmethod
    def Transpose(matrix: Matrix4x4) -> Matrix4x4: ...
    
    @staticmethod
    def get_Identity() -> Matrix4x4: ...
    
    def get_IsIdentity(self) -> BooleanType: ...
    
    def get_Translation(self) -> Vector3: ...
    
    @staticmethod
    def op_Addition(value1: Matrix4x4, value2: Matrix4x4) -> Matrix4x4: ...
    
    @staticmethod
    def op_Equality(value1: Matrix4x4, value2: Matrix4x4) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(value1: Matrix4x4, value2: Matrix4x4) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Multiply(value1: Matrix4x4, value2: Matrix4x4) -> Matrix4x4: ...
    
    @staticmethod
    @overload
    def op_Multiply(value1: Matrix4x4, value2: FloatType) -> Matrix4x4: ...
    
    @staticmethod
    def op_Subtraction(value1: Matrix4x4, value2: Matrix4x4) -> Matrix4x4: ...
    
    @staticmethod
    def op_UnaryNegation(value: Matrix4x4) -> Matrix4x4: ...
    
    def set_Translation(self, value: Vector3) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Plane(ValueType, IEquatable[Plane]):
    # ---------- Fields ---------- #
    
    @property
    def D(self) -> FloatType: ...
    
    @D.setter
    def D(self, value: FloatType) -> None: ...
    
    @property
    def Normal(self) -> Vector3: ...
    
    @Normal.setter
    def Normal(self, value: Vector3) -> None: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, x: FloatType, y: FloatType, z: FloatType, d: FloatType): ...
    
    @overload
    def __init__(self, normal: Vector3, d: FloatType): ...
    
    @overload
    def __init__(self, value: Vector4): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateFromVertices(point1: Vector3, point2: Vector3, point3: Vector3) -> Plane: ...
    
    @staticmethod
    def Dot(plane: Plane, value: Vector4) -> FloatType: ...
    
    @staticmethod
    def DotCoordinate(plane: Plane, value: Vector3) -> FloatType: ...
    
    @staticmethod
    def DotNormal(plane: Plane, value: Vector3) -> FloatType: ...
    
    @overload
    def Equals(self, other: Plane) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def Normalize(value: Plane) -> Plane: ...
    
    def ToString(self) -> StringType: ...
    
    @staticmethod
    @overload
    def Transform(plane: Plane, matrix: Matrix4x4) -> Plane: ...
    
    @staticmethod
    @overload
    def Transform(plane: Plane, rotation: Quaternion) -> Plane: ...
    
    @staticmethod
    def op_Equality(value1: Plane, value2: Plane) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(value1: Plane, value2: Plane) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Quaternion(ValueType, IEquatable[Quaternion]):
    # ---------- Fields ---------- #
    
    @property
    def W(self) -> FloatType: ...
    
    @W.setter
    def W(self, value: FloatType) -> None: ...
    
    @property
    def X(self) -> FloatType: ...
    
    @X.setter
    def X(self, value: FloatType) -> None: ...
    
    @property
    def Y(self) -> FloatType: ...
    
    @Y.setter
    def Y(self, value: FloatType) -> None: ...
    
    @property
    def Z(self) -> FloatType: ...
    
    @Z.setter
    def Z(self, value: FloatType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, x: FloatType, y: FloatType, z: FloatType, w: FloatType): ...
    
    @overload
    def __init__(self, vectorPart: Vector3, scalarPart: FloatType): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Identity() -> Quaternion: ...
    
    @property
    def IsIdentity(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Add(value1: Quaternion, value2: Quaternion) -> Quaternion: ...
    
    @staticmethod
    def Concatenate(value1: Quaternion, value2: Quaternion) -> Quaternion: ...
    
    @staticmethod
    def Conjugate(value: Quaternion) -> Quaternion: ...
    
    @staticmethod
    def CreateFromAxisAngle(axis: Vector3, angle: FloatType) -> Quaternion: ...
    
    @staticmethod
    def CreateFromRotationMatrix(matrix: Matrix4x4) -> Quaternion: ...
    
    @staticmethod
    def CreateFromYawPitchRoll(yaw: FloatType, pitch: FloatType, roll: FloatType) -> Quaternion: ...
    
    @staticmethod
    def Divide(value1: Quaternion, value2: Quaternion) -> Quaternion: ...
    
    @staticmethod
    def Dot(quaternion1: Quaternion, quaternion2: Quaternion) -> FloatType: ...
    
    @overload
    def Equals(self, other: Quaternion) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def Inverse(value: Quaternion) -> Quaternion: ...
    
    def Length(self) -> FloatType: ...
    
    def LengthSquared(self) -> FloatType: ...
    
    @staticmethod
    def Lerp(quaternion1: Quaternion, quaternion2: Quaternion, amount: FloatType) -> Quaternion: ...
    
    @staticmethod
    @overload
    def Multiply(value1: Quaternion, value2: Quaternion) -> Quaternion: ...
    
    @staticmethod
    @overload
    def Multiply(value1: Quaternion, value2: FloatType) -> Quaternion: ...
    
    @staticmethod
    def Negate(value: Quaternion) -> Quaternion: ...
    
    @staticmethod
    def Normalize(value: Quaternion) -> Quaternion: ...
    
    @staticmethod
    def Slerp(quaternion1: Quaternion, quaternion2: Quaternion, amount: FloatType) -> Quaternion: ...
    
    @staticmethod
    def Subtract(value1: Quaternion, value2: Quaternion) -> Quaternion: ...
    
    def ToString(self) -> StringType: ...
    
    @staticmethod
    def get_Identity() -> Quaternion: ...
    
    def get_IsIdentity(self) -> BooleanType: ...
    
    @staticmethod
    def op_Addition(value1: Quaternion, value2: Quaternion) -> Quaternion: ...
    
    @staticmethod
    def op_Division(value1: Quaternion, value2: Quaternion) -> Quaternion: ...
    
    @staticmethod
    def op_Equality(value1: Quaternion, value2: Quaternion) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(value1: Quaternion, value2: Quaternion) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Multiply(value1: Quaternion, value2: Quaternion) -> Quaternion: ...
    
    @staticmethod
    @overload
    def op_Multiply(value1: Quaternion, value2: FloatType) -> Quaternion: ...
    
    @staticmethod
    def op_Subtraction(value1: Quaternion, value2: Quaternion) -> Quaternion: ...
    
    @staticmethod
    def op_UnaryNegation(value: Quaternion) -> Quaternion: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Vector2(ValueType, IEquatable[Vector2], IFormattable):
    # ---------- Fields ---------- #
    
    @property
    def X(self) -> FloatType: ...
    
    @X.setter
    def X(self, value: FloatType) -> None: ...
    
    @property
    def Y(self) -> FloatType: ...
    
    @Y.setter
    def Y(self, value: FloatType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, value: FloatType): ...
    
    @overload
    def __init__(self, x: FloatType, y: FloatType): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def One() -> Vector2: ...
    
    @staticmethod
    @property
    def UnitX() -> Vector2: ...
    
    @staticmethod
    @property
    def UnitY() -> Vector2: ...
    
    @staticmethod
    @property
    def Zero() -> Vector2: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Abs(value: Vector2) -> Vector2: ...
    
    @staticmethod
    def Add(left: Vector2, right: Vector2) -> Vector2: ...
    
    @staticmethod
    def Clamp(value1: Vector2, min: Vector2, max: Vector2) -> Vector2: ...
    
    @overload
    def CopyTo(self, array: ArrayType[FloatType]) -> VoidType: ...
    
    @overload
    def CopyTo(self, array: ArrayType[FloatType], index: IntType) -> VoidType: ...
    
    @staticmethod
    def Distance(value1: Vector2, value2: Vector2) -> FloatType: ...
    
    @staticmethod
    def DistanceSquared(value1: Vector2, value2: Vector2) -> FloatType: ...
    
    @staticmethod
    @overload
    def Divide(left: Vector2, right: Vector2) -> Vector2: ...
    
    @staticmethod
    @overload
    def Divide(left: Vector2, divisor: FloatType) -> Vector2: ...
    
    @staticmethod
    def Dot(value1: Vector2, value2: Vector2) -> FloatType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: Vector2) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Length(self) -> FloatType: ...
    
    def LengthSquared(self) -> FloatType: ...
    
    @staticmethod
    def Lerp(value1: Vector2, value2: Vector2, amount: FloatType) -> Vector2: ...
    
    @staticmethod
    def Max(value1: Vector2, value2: Vector2) -> Vector2: ...
    
    @staticmethod
    def Min(value1: Vector2, value2: Vector2) -> Vector2: ...
    
    @staticmethod
    @overload
    def Multiply(left: Vector2, right: Vector2) -> Vector2: ...
    
    @staticmethod
    @overload
    def Multiply(left: Vector2, right: FloatType) -> Vector2: ...
    
    @staticmethod
    @overload
    def Multiply(left: FloatType, right: Vector2) -> Vector2: ...
    
    @staticmethod
    def Negate(value: Vector2) -> Vector2: ...
    
    @staticmethod
    def Normalize(value: Vector2) -> Vector2: ...
    
    @staticmethod
    def Reflect(vector: Vector2, normal: Vector2) -> Vector2: ...
    
    @staticmethod
    def SquareRoot(value: Vector2) -> Vector2: ...
    
    @staticmethod
    def Subtract(left: Vector2, right: Vector2) -> Vector2: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, formatProvider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @staticmethod
    @overload
    def Transform(position: Vector2, matrix: Matrix3x2) -> Vector2: ...
    
    @staticmethod
    @overload
    def Transform(position: Vector2, matrix: Matrix4x4) -> Vector2: ...
    
    @staticmethod
    @overload
    def Transform(value: Vector2, rotation: Quaternion) -> Vector2: ...
    
    @staticmethod
    @overload
    def TransformNormal(normal: Vector2, matrix: Matrix3x2) -> Vector2: ...
    
    @staticmethod
    @overload
    def TransformNormal(normal: Vector2, matrix: Matrix4x4) -> Vector2: ...
    
    @staticmethod
    def get_One() -> Vector2: ...
    
    @staticmethod
    def get_UnitX() -> Vector2: ...
    
    @staticmethod
    def get_UnitY() -> Vector2: ...
    
    @staticmethod
    def get_Zero() -> Vector2: ...
    
    @staticmethod
    def op_Addition(left: Vector2, right: Vector2) -> Vector2: ...
    
    @staticmethod
    @overload
    def op_Division(left: Vector2, right: Vector2) -> Vector2: ...
    
    @staticmethod
    @overload
    def op_Division(value1: Vector2, value2: FloatType) -> Vector2: ...
    
    @staticmethod
    def op_Equality(left: Vector2, right: Vector2) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: Vector2, right: Vector2) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Multiply(left: Vector2, right: Vector2) -> Vector2: ...
    
    @staticmethod
    @overload
    def op_Multiply(left: FloatType, right: Vector2) -> Vector2: ...
    
    @staticmethod
    @overload
    def op_Multiply(left: Vector2, right: FloatType) -> Vector2: ...
    
    @staticmethod
    def op_Subtraction(left: Vector2, right: Vector2) -> Vector2: ...
    
    @staticmethod
    def op_UnaryNegation(value: Vector2) -> Vector2: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Vector3(ValueType, IEquatable[Vector3], IFormattable):
    # ---------- Fields ---------- #
    
    @property
    def X(self) -> FloatType: ...
    
    @X.setter
    def X(self, value: FloatType) -> None: ...
    
    @property
    def Y(self) -> FloatType: ...
    
    @Y.setter
    def Y(self, value: FloatType) -> None: ...
    
    @property
    def Z(self) -> FloatType: ...
    
    @Z.setter
    def Z(self, value: FloatType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, value: FloatType): ...
    
    @overload
    def __init__(self, value: Vector2, z: FloatType): ...
    
    @overload
    def __init__(self, x: FloatType, y: FloatType, z: FloatType): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def One() -> Vector3: ...
    
    @staticmethod
    @property
    def UnitX() -> Vector3: ...
    
    @staticmethod
    @property
    def UnitY() -> Vector3: ...
    
    @staticmethod
    @property
    def UnitZ() -> Vector3: ...
    
    @staticmethod
    @property
    def Zero() -> Vector3: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Abs(value: Vector3) -> Vector3: ...
    
    @staticmethod
    def Add(left: Vector3, right: Vector3) -> Vector3: ...
    
    @staticmethod
    def Clamp(value1: Vector3, min: Vector3, max: Vector3) -> Vector3: ...
    
    @overload
    def CopyTo(self, array: ArrayType[FloatType]) -> VoidType: ...
    
    @overload
    def CopyTo(self, array: ArrayType[FloatType], index: IntType) -> VoidType: ...
    
    @staticmethod
    def Cross(vector1: Vector3, vector2: Vector3) -> Vector3: ...
    
    @staticmethod
    def Distance(value1: Vector3, value2: Vector3) -> FloatType: ...
    
    @staticmethod
    def DistanceSquared(value1: Vector3, value2: Vector3) -> FloatType: ...
    
    @staticmethod
    @overload
    def Divide(left: Vector3, right: Vector3) -> Vector3: ...
    
    @staticmethod
    @overload
    def Divide(left: Vector3, divisor: FloatType) -> Vector3: ...
    
    @staticmethod
    def Dot(vector1: Vector3, vector2: Vector3) -> FloatType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: Vector3) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Length(self) -> FloatType: ...
    
    def LengthSquared(self) -> FloatType: ...
    
    @staticmethod
    def Lerp(value1: Vector3, value2: Vector3, amount: FloatType) -> Vector3: ...
    
    @staticmethod
    def Max(value1: Vector3, value2: Vector3) -> Vector3: ...
    
    @staticmethod
    def Min(value1: Vector3, value2: Vector3) -> Vector3: ...
    
    @staticmethod
    @overload
    def Multiply(left: Vector3, right: Vector3) -> Vector3: ...
    
    @staticmethod
    @overload
    def Multiply(left: Vector3, right: FloatType) -> Vector3: ...
    
    @staticmethod
    @overload
    def Multiply(left: FloatType, right: Vector3) -> Vector3: ...
    
    @staticmethod
    def Negate(value: Vector3) -> Vector3: ...
    
    @staticmethod
    def Normalize(value: Vector3) -> Vector3: ...
    
    @staticmethod
    def Reflect(vector: Vector3, normal: Vector3) -> Vector3: ...
    
    @staticmethod
    def SquareRoot(value: Vector3) -> Vector3: ...
    
    @staticmethod
    def Subtract(left: Vector3, right: Vector3) -> Vector3: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, formatProvider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @staticmethod
    @overload
    def Transform(position: Vector3, matrix: Matrix4x4) -> Vector3: ...
    
    @staticmethod
    @overload
    def Transform(value: Vector3, rotation: Quaternion) -> Vector3: ...
    
    @staticmethod
    def TransformNormal(normal: Vector3, matrix: Matrix4x4) -> Vector3: ...
    
    @staticmethod
    def get_One() -> Vector3: ...
    
    @staticmethod
    def get_UnitX() -> Vector3: ...
    
    @staticmethod
    def get_UnitY() -> Vector3: ...
    
    @staticmethod
    def get_UnitZ() -> Vector3: ...
    
    @staticmethod
    def get_Zero() -> Vector3: ...
    
    @staticmethod
    def op_Addition(left: Vector3, right: Vector3) -> Vector3: ...
    
    @staticmethod
    @overload
    def op_Division(left: Vector3, right: Vector3) -> Vector3: ...
    
    @staticmethod
    @overload
    def op_Division(value1: Vector3, value2: FloatType) -> Vector3: ...
    
    @staticmethod
    def op_Equality(left: Vector3, right: Vector3) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: Vector3, right: Vector3) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Multiply(left: Vector3, right: Vector3) -> Vector3: ...
    
    @staticmethod
    @overload
    def op_Multiply(left: Vector3, right: FloatType) -> Vector3: ...
    
    @staticmethod
    @overload
    def op_Multiply(left: FloatType, right: Vector3) -> Vector3: ...
    
    @staticmethod
    def op_Subtraction(left: Vector3, right: Vector3) -> Vector3: ...
    
    @staticmethod
    def op_UnaryNegation(value: Vector3) -> Vector3: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Vector4(ValueType, IEquatable[Vector4], IFormattable):
    # ---------- Fields ---------- #
    
    @property
    def W(self) -> FloatType: ...
    
    @W.setter
    def W(self, value: FloatType) -> None: ...
    
    @property
    def X(self) -> FloatType: ...
    
    @X.setter
    def X(self, value: FloatType) -> None: ...
    
    @property
    def Y(self) -> FloatType: ...
    
    @Y.setter
    def Y(self, value: FloatType) -> None: ...
    
    @property
    def Z(self) -> FloatType: ...
    
    @Z.setter
    def Z(self, value: FloatType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, value: FloatType): ...
    
    @overload
    def __init__(self, x: FloatType, y: FloatType, z: FloatType, w: FloatType): ...
    
    @overload
    def __init__(self, value: Vector2, z: FloatType, w: FloatType): ...
    
    @overload
    def __init__(self, value: Vector3, w: FloatType): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def One() -> Vector4: ...
    
    @staticmethod
    @property
    def UnitW() -> Vector4: ...
    
    @staticmethod
    @property
    def UnitX() -> Vector4: ...
    
    @staticmethod
    @property
    def UnitY() -> Vector4: ...
    
    @staticmethod
    @property
    def UnitZ() -> Vector4: ...
    
    @staticmethod
    @property
    def Zero() -> Vector4: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Abs(value: Vector4) -> Vector4: ...
    
    @staticmethod
    def Add(left: Vector4, right: Vector4) -> Vector4: ...
    
    @staticmethod
    def Clamp(value1: Vector4, min: Vector4, max: Vector4) -> Vector4: ...
    
    @overload
    def CopyTo(self, array: ArrayType[FloatType]) -> VoidType: ...
    
    @overload
    def CopyTo(self, array: ArrayType[FloatType], index: IntType) -> VoidType: ...
    
    @staticmethod
    def Distance(value1: Vector4, value2: Vector4) -> FloatType: ...
    
    @staticmethod
    def DistanceSquared(value1: Vector4, value2: Vector4) -> FloatType: ...
    
    @staticmethod
    @overload
    def Divide(left: Vector4, right: Vector4) -> Vector4: ...
    
    @staticmethod
    @overload
    def Divide(left: Vector4, divisor: FloatType) -> Vector4: ...
    
    @staticmethod
    def Dot(vector1: Vector4, vector2: Vector4) -> FloatType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: Vector4) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Length(self) -> FloatType: ...
    
    def LengthSquared(self) -> FloatType: ...
    
    @staticmethod
    def Lerp(value1: Vector4, value2: Vector4, amount: FloatType) -> Vector4: ...
    
    @staticmethod
    def Max(value1: Vector4, value2: Vector4) -> Vector4: ...
    
    @staticmethod
    def Min(value1: Vector4, value2: Vector4) -> Vector4: ...
    
    @staticmethod
    @overload
    def Multiply(left: Vector4, right: Vector4) -> Vector4: ...
    
    @staticmethod
    @overload
    def Multiply(left: Vector4, right: FloatType) -> Vector4: ...
    
    @staticmethod
    @overload
    def Multiply(left: FloatType, right: Vector4) -> Vector4: ...
    
    @staticmethod
    def Negate(value: Vector4) -> Vector4: ...
    
    @staticmethod
    def Normalize(vector: Vector4) -> Vector4: ...
    
    @staticmethod
    def SquareRoot(value: Vector4) -> Vector4: ...
    
    @staticmethod
    def Subtract(left: Vector4, right: Vector4) -> Vector4: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, formatProvider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @staticmethod
    @overload
    def Transform(position: Vector2, matrix: Matrix4x4) -> Vector4: ...
    
    @staticmethod
    @overload
    def Transform(position: Vector3, matrix: Matrix4x4) -> Vector4: ...
    
    @staticmethod
    @overload
    def Transform(vector: Vector4, matrix: Matrix4x4) -> Vector4: ...
    
    @staticmethod
    @overload
    def Transform(value: Vector2, rotation: Quaternion) -> Vector4: ...
    
    @staticmethod
    @overload
    def Transform(value: Vector3, rotation: Quaternion) -> Vector4: ...
    
    @staticmethod
    @overload
    def Transform(value: Vector4, rotation: Quaternion) -> Vector4: ...
    
    @staticmethod
    def get_One() -> Vector4: ...
    
    @staticmethod
    def get_UnitW() -> Vector4: ...
    
    @staticmethod
    def get_UnitX() -> Vector4: ...
    
    @staticmethod
    def get_UnitY() -> Vector4: ...
    
    @staticmethod
    def get_UnitZ() -> Vector4: ...
    
    @staticmethod
    def get_Zero() -> Vector4: ...
    
    @staticmethod
    def op_Addition(left: Vector4, right: Vector4) -> Vector4: ...
    
    @staticmethod
    @overload
    def op_Division(left: Vector4, right: Vector4) -> Vector4: ...
    
    @staticmethod
    @overload
    def op_Division(value1: Vector4, value2: FloatType) -> Vector4: ...
    
    @staticmethod
    def op_Equality(left: Vector4, right: Vector4) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: Vector4, right: Vector4) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Multiply(left: Vector4, right: Vector4) -> Vector4: ...
    
    @staticmethod
    @overload
    def op_Multiply(left: Vector4, right: FloatType) -> Vector4: ...
    
    @staticmethod
    @overload
    def op_Multiply(left: FloatType, right: Vector4) -> Vector4: ...
    
    @staticmethod
    def op_Subtraction(left: Vector4, right: Vector4) -> Vector4: ...
    
    @staticmethod
    def op_UnaryNegation(value: Vector4) -> Vector4: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Interfaces

# No Enums

# No Delegates

__all__ = [
    BigNumber,
    HashCodeHelper,
    JitIntrinsicAttribute,
    NumericsHelpers,
    Vector,
    BigInteger,
    BigIntegerBuilder,
    Complex,
    DoubleUlong,
    Matrix3x2,
    Matrix4x4,
    Plane,
    Quaternion,
    Vector2,
    Vector3,
    Vector4,
]
