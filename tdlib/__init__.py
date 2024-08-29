try:
    from importlib import resources
    resources.files
except (ImportError, AttributeError):
    import importlib_resources as resources

def _get_tdjson_lib_path() -> str:

    lib_name = "libtdjson.so"

    return str(resources.files("tdlib").joinpath(lib_name))
