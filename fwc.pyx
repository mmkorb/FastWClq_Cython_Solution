# cython: c_string_type=unicode, c_string_encoding=utf8

import cython
from cython.parallel import prange

from libcpp.string cimport string
from libcpp.vector cimport vector


cdef extern from "FastWClq-codes/fwc.hpp":
    cdef cppclass fwc:
        fwc() except +
        vector[long] get_best_solution(string) 

cdef class pyfwc:
    cdef fwc *thisptr      # hold a C++ instance which we're wrapping

    def __cinit__(self):
        self.thisptr = new fwc()

    def __dealloc__(self):
        del self.thisptr

    def get_best_solution(self, string str1):
        return list(self.thisptr.get_best_solution(str1))