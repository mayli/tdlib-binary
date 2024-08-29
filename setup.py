import os
import shutil
from pathlib import Path
from subprocess import check_call

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext as build_ext_orig
from wheel.bdist_wheel import bdist_wheel

EXTRA = "-DCMAKE_TOOLCHAIN_FILE=%s/vcpkg/scripts/buildsystems/vcpkg.cmake" % os.getcwd()


def get_version():
    # project(TDLib VERSION 1.8.35 LANGUAGES CXX C)
    with open("tdlight/CMakeLists.txt") as fd:
        for line in fd:
            if line.startswith("project(TDLib VERSION"):
                return line.split()[2]
    return "0.0.1"


class bdist_wheel_abi3(bdist_wheel):
    def get_tag(self):
        python, abi, plat = super().get_tag()

        if python.startswith("cp"):
            # on CPython, our wheels are abi3 and compatible back to 3.6
            return python, "abi3", plat

        return python, abi, plat


class build_ext(build_ext_orig):
    def run(self):
        for f in Path('tdlib/lib/').glob('*'):
            if f.is_symlink():
                # readink Added in version 3.9.
                src = Path('tdlib/lib/') / os.readlink(f)
                f.unlink()
                src.rename(f)


def read_readme():
    with open(
        os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8"
    ) as f:
        return f.read()


setup(
    name="tdlib-binary",
    version=get_version(),
    description="tdlib binary build",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    author="tdlib-binary dev",
    packages=["tdlib"],
    ext_modules=[Extension("tdlib", [])],
    cmdclass={
        "build_ext": build_ext,
        "bdist_wheel": bdist_wheel_abi3,
    },
    package_data={
        "tdlib": ["lib/*"],
    },
    install_requires=[
        'importlib-resources>=1.3; python_version < "3.9"',
    ],
)
