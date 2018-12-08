from setuptools import setup, find_packages

setup(
    name='acl',
    version='0.1',
    py_modules=['acl'],
    packages=find_packages(),
    install_requires=[
        'Click', 'robobrowser', 'bs4', 'tabulate'
    ],
    entry_points='''
        [console_scripts]
        acl=source:attendance
    ''',
)