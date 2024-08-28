from ctypes import CDLL, CFUNCTYPE, c_int, c_char_p, c_double, c_void_p, c_longlong
from tdlib import _get_tdjson_lib_path

tdjson = CDLL(_get_tdjson_lib_path())

client_create = tdjson.td_json_client_create
client_create.restype = c_void_p
client_create.argtypes = []

client = client_create()
print(client)
