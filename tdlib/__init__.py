import json
import logging
import platform
from ctypes import CDLL, CFUNCTYPE, c_int, c_char_p, c_double, c_void_p, c_longlong
from typing import Any, Dict, Optional, Union
import importlib.resources

def _get_tdjson_lib_path() -> str:

    lib_name = "libtdjson.so"

    return str(importlib.resources.files("tdlib").joinpath(lib_name))
