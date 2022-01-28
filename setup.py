from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='stubgen',
    version='1.1.1',
    description='A library for generating stubs of .NET libraries',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Mimer29or40/pythonnet-stubs',
    author='Ryan Smith',
    author_email='Ryan.Smith1215@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Version Control :: Git',
        'Topic :: Utilities',
    ],
    keywords='pythonnet, generation',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.8',
    install_requires=[
        'pythonnet==2.5.2',
        'docopt',
    ],
    extras_require={
        'dev': [
            'setuptools',
            'wheel',
            'tox',
        ],
    },
    project_urls={
        'Source':      'https://github.aepsc.com/s316353/pyPIAF',
        'Bug Reports': 'https://github.aepsc.com/s316353/pyPIAF/issues',
    },
)
