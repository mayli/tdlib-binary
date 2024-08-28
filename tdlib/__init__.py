import importlib.resources

def _get_tdjson_lib_path() -> str:

    lib_name = "libtdjson.so"

    return str(importlib.resources.files("tdlib").joinpath(lib_name))
