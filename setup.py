import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "lang-detect",
    version = "0.0.1",
    author = "Mingli Yuan",
    author_email = "mingli.yuan@gmail.com",
    description = ("a tool to detecting the language for a small piece of "
        "unicode text without any dependency to other libraries."),
    license = "BSD",
    keywords = "nlp language unicode",
    url = "https://github.com/braingnp-org/lang-detect",
    packages = find_packages('python'),
    package_dir = {'':'python'},
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    include_package_data=True,
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt']
    }
)

