from typing import List

DEFAULT_OUTPUT_PATH: str = 'stubs'

PATHS: List[str] = [
    # | Local Binaries
]

ASSEMBLIES: List[str] = [
    # | System
    'System',
    'System.Collections',
    'System.Collections.Generic',
    'System.ComponentModel',
    'System.Configuration',
    'System.Data',
    'System.Data.Common',
    'System.Drawing',
    'System.IO',
    'System.Media',
    'System.Net',
    'System.Reflection',
    'System.Runtime',
    'System.Security',
    'System.Threading',
    'System.Web',
    'System.Windows',
    'System.Windows.Forms',
    'System.Xaml',
    'System.Xml',
]

BUILT_INS: List[str] = [
    'clr',
]

ASSEMBLIES.extend(BUILT_INS)
ASSEMBLIES.sort()
