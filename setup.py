"""
setup.py: Install simtk.units
"""
from distutils.core import setup
try:
   from distutils.command.build_py import build_py_2to3 \
        as build_py
except ImportError:
   from distutils.command.build_py import build_py

major_version_num='0'
minor_version_num='2'

def doSetup():
    setupKeywords = {}
    setupKeywords["name"]              = "simtk.unit"
    setupKeywords["version"]           = "%s.%s" % (major_version_num, minor_version_num)
    setupKeywords["author"]            = "Christopher M. Bruns"
    setupKeywords["author_email"]      = "cmbruns@stanford.edu"
    setupKeywords["cmdclass"]          = {'build_py': build_py}
    setupKeywords["url"]               = "https://github.com/rmcgibbo/simtk.unit"
    setupKeywords["license"]           = "Python Software Foundation License (BSD-like)"
    setupKeywords["packages"]          = ["simtk", "simtk.unit"]
    setupKeywords["data_files"]        = []
    setupKeywords["platforms"]         = ["Linux", "Mac OS X", "Windows"]
    setupKeywords["description"]       = "Units for python"
    setupKeywords["long_description"]  = \
    """Units-aware quantity classes for python
    """

    setup(**setupKeywords)
    

if __name__ == '__main__':
    doSetup()
