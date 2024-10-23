from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyserial"
    ],
    author="Mekyle Hemani",
    description="A tool with easy prebuilt function to communicate through PySerial",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Mekyle-Hemani/SimpleSerial",
)
