import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bus",
    version="0.0.1",
    author="Joe Coburn",
    author_email="joe@scholarpack.com",
    description="Aggregate JSON data together",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CoburnJoe/bus",
    packages=["bus"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha  ",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
