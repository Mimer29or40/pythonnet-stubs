import requests
from bs4 import BeautifulSoup

API = 'net'
VERSION = '6.0'

BASE_URL = 'https://docs.microsoft.com/en-us/dotnet/api/'


DEFAULT_NAMESPACES = [
    'System'
    'System.Buffers'
    'System.Buffers.Binary'
    'System.Buffers.Text'
    'System.CodeDom.Compiler'
    'System.Collections'
    'System.Collections.Concurrent'
    'System.Collections.Generic'
    'System.Collections.Immutable'
    'System.Collections.ObjectModel'
    'System.Collections.Specialized'
    'System.ComponentModel'
    'System.ComponentModel.DataAnnotations'
    'System.ComponentModel.DataAnnotations.Schema'
    'System.ComponentModel.Design'
    'System.ComponentModel.Design.Serialization'
    'System.Configuration.Assemblies'
    'System.Data'
    'System.Data.Common'
    'System.Data.SqlTypes'
    'System.Diagnostics'
    'System.Diagnostics.CodeAnalysis'
    'System.Diagnostics.Contracts'
    'System.Diagnostics.Metrics'
    'System.Diagnostics.SymbolStore'
    'System.Diagnostics.Tracing'
    'System.Drawing'
    'System.Dynamic'
    'System.Formats.Asn1'
    'System.Globalization'
    'System.IO'
    'System.IO.Compression'
    'System.IO.Enumeration'
    'System.IO.IsolatedStorage'
    'System.IO.MemoryMappedFiles'
    'System.IO.Pipes'
    'System.Linq'
    'System.Linq.Expressions'
    'System.Net'
    'System.Net.Cache'
    'System.Net.Http'
    'System.Net.Http.Headers'
    'System.Net.Http.Json'
    'System.Net.Mail'
    'System.Net.Mime'
    'System.Net.NetworkInformation'
    'System.Net.Security'
    'System.Net.Sockets'
    'System.Net.WebSockets'
    'System.Numerics'
    'System.Reflection'
    'System.Reflection.Emit'
    'System.Reflection.Metadata'
    'System.Reflection.Metadata.Ecma335'
    'System.Reflection.PortableExecutable'
    'System.Resources'
    'System.Runtime'
    'System.Runtime.CompilerServices'
    'System.Runtime.ConstrainedExecution'
    'System.Runtime.ExceptionServices'
    'System.Runtime.InteropServices'
    'System.Runtime.InteropServices.ComTypes'
    'System.Runtime.InteropServices.ObjectiveC'
    'System.Runtime.Intrinsics'
    'System.Runtime.Intrinsics.Arm'
    'System.Runtime.Intrinsics.X86'
    'System.Runtime.Loader'
    'System.Runtime.Remoting'
    'System.Runtime.Serialization'
    'System.Runtime.Serialization.Formatters'
    'System.Runtime.Serialization.Formatters.Binary'
    'System.Runtime.Serialization.Json'
    'System.Runtime.Versioning'
    'System.Security'
    'System.Security.AccessControl'
    'System.Security.Authentication'
    'System.Security.Authentication.ExtendedProtection'
    'System.Security.Claims'
    'System.Security.Cryptography'
    'System.Security.Cryptography.X509Certificates'
    'System.Security.Permissions'
    'System.Security.Policy'
    'System.Security.Principal'
    'System.Text'
    'System.Text.Encodings.Web'
    'System.Text.Json'
    'System.Text.Json.Nodes'
    'System.Text.Json.Serialization'
    'System.Text.Json.Serialization.Metadata'
    'System.Text.RegularExpressions'
    'System.Text.Unicode'
    'System.Threading'
    'System.Threading.Channels'
    'System.Threading.Tasks'
    'System.Threading.Tasks.Dataflow'
    'System.Threading.Tasks.Sources'
    'System.Timers'
    'System.Transactions'
    'System.Web'
    'System.Windows.Input'
    'System.Windows.Markup'
    'System.Xml'
    'System.Xml.Linq'
    'System.Xml.Resolvers'
    'System.Xml.Schema'
    'System.Xml.Serialization'
    'System.Xml.XPath'
    'System.Xml.Xsl'
]


def extract_namespace(namespace: str):
    ext = f'{namespace}?view={API}-{VERSION}'
    
    page = requests.get(BASE_URL + ext)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup.new_tag()
    for section in soup.find_all('h2'):
        name = section.get_text().strip()
        print(name)
        for row in section.find_all_next('tr'):
            attribute_name_tag = row.find_next('a')
            attribute_desc_tag = row.find_next('p')
            
            attribute_name = attribute_name_tag.get_text().strip()
            attribute_url = BASE_URL + attribute_name_tag['href']
            attribute_desc = attribute_desc_tag.get_text().strip()
            print(attribute_name, attribute_url, attribute_desc)


if __name__ == '__main__':
    extract_namespace('system')
