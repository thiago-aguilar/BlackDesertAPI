from setuptools import setup
import setuptools

# read description
with open("README.md", "r") as fh:
    long_description = fh.read()

# read requirements
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="Black_Desert_Item_Finder",
    version="0.1",
    author="Thiago Borges Aguilar",
    author_email="thiago.aaguilar@gmail.com",
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=required,
    packages=setuptools.find_packages()
)