from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("D3M09.pyx")
)
