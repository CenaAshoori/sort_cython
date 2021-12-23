from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

sourcefiles=['bubblesort_caller.pyx']
ext_modules=[Extension('bubblesort_caller',
                       sourcefiles
                       )]
setup(
    name='Bubblesort',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)