import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "Readme.md").read_text()

# This call to setup() does all the work
setup(
    name="EasyPySqlite",
    version="0.0.4",
    description="Simplify Sqlite operations",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mohaelder/pysqlite",
    author="Yasushi Oh",
    author_email="yoh@ucsd.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["EasyPySqlite"],
    include_package_data=True,
    entry_points={
    },
)