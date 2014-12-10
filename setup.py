from setuptools import setup, find_packages

setup(
    name="testtrackpro",
    version='1.0.3',
    description="Python interface to TestTrackPro SOAP API",
    long_description=open('README.rst').read(),
    url="https://github.com/umank/python-testtrackpro3",
    author="Umankshree Behera",
    author_email="umankshree@gmail.com",
    original_author="Anthony Burchette",
    original_author_email="awburchette+testtrackpro@gmail.com",
    license="BSD",
    py_modules=['testtrackpro'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=['suds-jurko>=0.6',],
    keywords=["testtrack", "testtrackpro", "soap", "suds"],
)
