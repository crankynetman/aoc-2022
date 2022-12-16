"""
Setup for AoC 2022 package
"""

import setuptools

setuptools.setup(
    name="aoc_2022_python",
    version="1.0.0",
    author="Chris Cummings",
    author_email="nouser@slash64.tech",
    description="A package for AoC 2022",
    url="https://github.com/crankynetman/aoc-2022",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires=">=3.6",
)
