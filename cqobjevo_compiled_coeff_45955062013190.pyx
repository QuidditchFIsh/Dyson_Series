#!python
#cython: language_level=3
# This file is generated automatically by QuTiP.

import numpy as np
cimport numpy as np
import scipy.special as spe
cimport cython
np.import_array()
cdef extern from "numpy/arrayobject.h" nogil:
    void PyDataMem_NEW_ZEROED(size_t size, size_t elsize)
    void PyArray_ENABLEFLAGS(np.ndarray arr, int flags)
from qutip.cy.spmatfuncs cimport spmvpy
from qutip.cy.inter cimport _spline_complex_t_second, _spline_complex_cte_second
from qutip.cy.inter cimport _spline_float_t_second, _spline_float_cte_second
from qutip.cy.inter cimport _step_float_cte, _step_complex_cte
from qutip.cy.inter cimport _step_float_t, _step_complex_t
from qutip.cy.interpolate cimport (interp, zinterp)
from qutip.cy.cqobjevo_factor cimport StrCoeff
from qutip.cy.cqobjevo cimport CQobjEvo
from qutip.cy.math cimport erf, zerf
from qutip.qobj import Qobj
cdef double pi = 3.14159265358979323

include '/home/nye/.local/lib/python3.7/site-packages/qutip/cy/complex_math.pxi'

cdef class CompiledStrCoeff(StrCoeff):

    cdef void _call_core(self, double t, complex * coeff):

        coeff[0] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[1] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[2] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[3] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[4] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[5] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[6] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[7] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[8] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[9] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[10] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[11] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[12] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[13] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[14] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[15] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[16] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[17] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[18] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[19] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[20] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[21] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[22] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[23] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[24] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[25] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[26] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[27] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[28] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[29] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[30] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[31] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[32] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[33] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[34] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[35] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[36] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[37] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[38] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[39] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[40] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[41] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[42] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[43] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[44] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[45] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[46] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[47] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[48] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[49] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[50] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[51] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[52] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[53] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[54] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[55] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[56] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[57] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[58] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[59] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[60] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[61] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[62] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[63] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[64] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[65] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[66] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[67] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[68] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[69] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[70] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[71] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[72] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[73] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[74] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[75] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[76] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[77] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[78] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[79] = cos(0*t) + (0 + 1j)*sin(0*t)
        coeff[80] = cos(0*t) + (0 + 1j)*sin(0*t)
