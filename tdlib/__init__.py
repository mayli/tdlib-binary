import os
import sys

try:
    from importlib import resources

    resources.files
except (ImportError, AttributeError):
    import importlib_resources as resources


def _get_tdjson_lib_path() -> str:
    if sys.platform.startswith("linux"):  # could be "linux", "linux2", "linux3", ...
        lib_name = "lib/libtdjson.so"
    elif sys.platform == "darwin":
        # MAC OS X
        lib_name = "lib/libtdjson.dylib"
    elif os.name == "nt":
        lib_name = "lib/libtdjson.dll"

    return str(resources.files("tdlib").joinpath(lib_name))
