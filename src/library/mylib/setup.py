import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mylib",
    version="0.1.0",
    author="TomTom MAPS Analytics",
    author_email="juancarlos.laria@tomtom.com",
    description="Example python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=['datetime']
)