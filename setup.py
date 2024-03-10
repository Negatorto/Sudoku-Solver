from setuptools import setup, find_packages

setup(
    name='Sudoku Solver',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PySide6',
        'PySide6_Addons',
        'PySide6_Essentials',
        'shiboken6'
    ],
)
