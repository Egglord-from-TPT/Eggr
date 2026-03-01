from setuptools import setup, find_packages

setup(
    name="eggr",
    version="1.0.1",
    packages=find_packages(),
    description="A Python package that extracts the longest reachable increasing sequence from a list of numbers where each step cannot exceed a specified distance.",
    author="",
    python_requires=">=3.7",
)
