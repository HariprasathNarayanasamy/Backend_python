import sys
from setuptools import setup, find_packages
NAME = "project1_server"
VERSION = "0.0.1"
REQUIRES = [ "smartutils>=1.0.1", "requests", "flask", "pycryptodome", "pycrypto"]
setup(
    name=NAME,
    version=VERSION,
    description="Usercred userid validator",
    author_email="support.netpol@telestratum.com",
    url="",
    keywords=["Usercred userid validator"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/*', 'etc/*', 'scripts/*', 'supervisor_scripts/*']},
    include_package_data=True,
    entry_points={'console_scripts': ['usercredsvalidator_server=usercredsvalidator_server.__main__:main']},
    long_description="""\ 
    Session handler service
    """
)
