from setuptools import setup, find_packages

setup(
    name="testtrackpro",
    version='1.0.2',
    description="Python interface to TestTrackPro SOAP API",
    long_description=open('README.rst').read(),
    url="https://github.com/awburchette/python-testtrackpro",
    author="Anthony Burchette",
    author_email="awburchette+testtrackpro@gmail.com",
    original_author="Doug Napoleone",
    original_author_email="doug.napoleone+testtrackpro@gmail.com",
    license="BSD",
    py_modules=['testtrackpro'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=['suds>=0.4',],
    keywords=["testtrack", "testtrackpro", "soap", "suds"],
)
