from typing import List

PATHS: List[str] = [

]

ASSEMBLIES: List[str] = [
    # | System
    'System',
    'System.Collections',
    'System.ComponentModel',
    'System.Configuration',
    'System.Data',
    'System.Data.Common',
    'System.Drawing',
    'System.IO',
    'System.Net',
    'System.Reflection',
    'System.Runtime',
    'System.Security',
    'System.Threading',
    'System.Web',
    'System.Windows',
    'System.Windows.Forms',
    'System.Xml',
]

BUILT_INS: List[str] = [
    'clr',
]

ASSEMBLIES.extend(BUILT_INS)
ASSEMBLIES.sort()
