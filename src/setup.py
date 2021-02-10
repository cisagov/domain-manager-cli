"""Setup tools."""
# Third-Party Libraries
from setuptools import setup

setup(
    name="domain-manager",
    version="0.1",
    py_modules=["domain-manager"],
    install_requires=[
        "Click",
        "colorama",
    ],
    entry_points="""
        [console_scripts]
        main=main:cli
    """,
)
