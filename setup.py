import setuptools
from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(

    # Needed to silence warnings (and to be a worthwhile package)
    name='Tbl.py',
    url='https://github.com',
    author='Jake',
    author_email='jakediserin@gmail.com',
    # Needed to actually package something
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Needed for dependencies
    install_requires=['requests' , 'bs4'],
    # *strongly* suggested for sharing
    version='2.0',
    # The license can be anything you like
    license='MIT',
    description='The official wrapper for Toxic\'s bot list API',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)