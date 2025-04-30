#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Configuración para la instalación del paquete MDPDFusion.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mdpdfusion",
    version="0.3.2",
    author="Alexander Oviedo Fadul",
    author_email="bladealex@gmail.com",
    description="Conversor de Markdown a PDF con múltiples interfaces",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bladealex9848/MDPDFusion",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "reportlab>=3.6.0",
        "pypandoc>=1.5.0",
        "streamlit>=1.10.0",
    ],
    extras_require={
        "gui": ["PyQt5>=5.15.0"],
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "mdpdfusion=mdpdfusion.__main__:main",
        ],
    },
)
