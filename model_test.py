from pprint import pprint

from stub_generator.logging import logger
from stub_generator.model2 import Namespace


if __name__ == '__main__':
    logger.info = print
    logger.debug = print
    
    namespace = Namespace('Test.Namespace', doc_string='Test Doc String')
    [namespace.add_py_import(i) for i in [
        'typing.Callable',
        'typing.Optional',
        'typing.Tuple',
        'typing.List',
        'typing.Dict',
        'typing.Union',
        'typing.Set',
    ]]

    [namespace.add_net_import(i) for i in [
        'System.Array',
        'System.Boolean',
        'System.Byte',
        'System.ICloneable',
        'System.Int32',
        'System.Object',
        'System.Collections.Generic.ICollection',
        'System.Collections.Generic.IComparer',
        'System.Collections.Generic.IEnumerable',
        'System.Collections.Generic.IEnumerator',
        'System.Collections.Generic.IEqualityComparer',
        'System.Collections.Generic.IList',
        'System.Collections.Generic.IReadOnlyCollection',
        'System.Collections.Generic.IReadOnlyList',
        'System.IO.Stream',
        'System.IO.TextReader',
        'System.IO.TextWriter',
        'System.Text.Encoding',
        'System.Text.NormalizationForm',
        'System.Text.StringBuilder',
    ]]
    
    pprint(namespace.to_lines(), width=160)
