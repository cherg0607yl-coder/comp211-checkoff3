import ctypes

lib = ctypes.CDLL("./libdouble.so")

lib.double_array.argtypes = [
    ctypes.POINTER(ctypes.c_int),
    ctypes.c_int
]
lib.double_array.restype = None

arr = (ctypes.c_int * 3)(1, 2, 3)
lib.double_array(arr, 3)

print(list(arr))