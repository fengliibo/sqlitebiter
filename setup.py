# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

import io
import os.path
import sys

import setuptools


MODULE_NAME = "sqlitebiter"
REPOSITORY_URL = "https://github.com/thombashi/{:s}".format(MODULE_NAME)
REQUIREMENT_DIR = "requirements"
ENCODING = "utf8"

pkg_info = {}


def need_pytest():
    return set(["pytest", "test", "ptr"]).intersection(sys.argv)


def get_release_command_class():
    try:
        from releasecmd import ReleaseCommand
    except ImportError:
        return {}

    return {"release": ReleaseCommand}


with open(os.path.join(MODULE_NAME, "__version__.py")) as f:
    exec(f.read(), pkg_info)

with io.open("README.rst", encoding=ENCODING) as fp:
    long_description = fp.read()

with io.open(os.path.join("docs", "pages", "introduction", "summary.txt"), encoding=ENCODING) as f:
    summary = f.read().strip()

with open(os.path.join(REQUIREMENT_DIR, "requirements.txt")) as f:
    install_requires = [line.strip() for line in f if line.strip()]

with open(os.path.join(REQUIREMENT_DIR, "test_requirements.txt")) as f:
    tests_requires = [line.strip() for line in f if line.strip()]

with open(os.path.join(REQUIREMENT_DIR, "build_requirements.txt")) as f:
    build_requires = [line.strip() for line in f if line.strip()]

with open(os.path.join(REQUIREMENT_DIR, "docs_requirements.txt")) as f:
    docs_requires = [line.strip() for line in f if line.strip()]

SETUPTOOLS_REQUIRES = ["setuptools>=38.3.0"]
PYTEST_RUNNER_REQUIRES = ["pytest-runner"] if need_pytest() else []

setuptools.setup(
    name=MODULE_NAME,
    version=pkg_info["__version__"],
    url=REPOSITORY_URL,

    author=pkg_info["__author__"],
    author_email=pkg_info["__email__"],
    description=summary,
    include_package_data=True,
    keywords=[
        "SQLite", "converter",
        "CSV", "Excel", "Google Sheets", "HTML", "JSON", "LTSV", "TSV",
    ],
    license=pkg_info["__license__"],
    long_description=long_description,
    packages=setuptools.find_packages(exclude=['test*']),
    project_urls={
        "Documentation": "https://{:s}.rtfd.io/".format(MODULE_NAME),
        "Tracker": "{:s}/issues".format(REPOSITORY_URL),
    },

    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*',
    install_requires=SETUPTOOLS_REQUIRES + install_requires,
    setup_requires=SETUPTOOLS_REQUIRES + PYTEST_RUNNER_REQUIRES,
    tests_require=tests_requires,
    extras_require={
        "build": build_requires,
        "docs": docs_requires,
        "gs": ["gspread", "oauth2client", "pyOpenSSL"],
        "mediawiki": ["pypandoc"],
        "release": ["releasecmd>=0.0.12"],
        "test": tests_requires,
    },

    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Jupyter",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Database",
    ],
    entry_points={
        "console_scripts": [
            "sqlitebiter=sqlitebiter.sqlitebiter:cmd",
        ],
    },
    cmdclass=get_release_command_class())
