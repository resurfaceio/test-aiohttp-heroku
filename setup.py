import os
import re

from setuptools import find_packages, setup

REGEXP = re.compile(r"^__version__\s=\s(.*)")


def read_file(name):
    with open(name) as fd:
        return fd.read()


def read_version():

    init_py = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "hackernews", "__init__.py"
    )

    with open(init_py) as f:
        for line in f:
            match = REGEXP.match(line)
            if match is not None:
                return match.group(1)
        else:
            msg = f"Cannot find version in ${init_py}"
            raise RuntimeError(msg)


setup(
    name="hackernews",
    version=read_version(),
    description="hackernews aiohttp and graphql",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_file("requirements.txt").splitlines(),
    zip_safe=False,
)
