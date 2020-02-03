from distutils.core import setup, Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

ext = Extension('fwc',
              sources=['fwc.pyx','FastWClq-codes/fwc.cpp'],
              extra_compile_args=['--std=c++11','-DNDEBU','-O3','--static'],
              language='c++')


setup(
    name = 'fwc',
    ext_modules=cythonize(ext),
    cmdclass = {'build_ext': build_ext}
)